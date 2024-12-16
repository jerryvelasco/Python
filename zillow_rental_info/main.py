from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

"""grabs rental prices from zillow url and enters them into a google sheets form"""
class ZillowRentalInfo:

    def __init__(self):
        #grabbed url after enter parameters 
        self.zillow_url = 'https://www.zillow.com/lower-east-side-manhattan-new-york-ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-74.009950378479%2C%22east%22%3A-73.964202621521%2C%22south%22%3A40.70313963188714%2C%22north%22%3A40.72812110502308%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A270875%2C%22regionType%22%3A8%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A14%2C%22usersSearchTerm%22%3A%22Lower%20East%20Side%20New%20York%20NY%22%7D'
        self.zillow_test_site = 'https://jerryvelasco.github.io/project/zillow_dummy_site.html'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }
        self.listings_address = []
        self.listings_price = []
        self.listings_link = []

        self.form_url = 'https://forms.gle/TrVqu37XuGbpuACn8'
        self.firefox_options = webdriver.FirefoxOptions()
        self.firefox_options.set_preference('detach', True)
        self.driver = webdriver.Firefox(options=self.firefox_options)


    """scrapes for the zillow data"""
    def get_rental_info(self):
        
        response = requests.get(url=self.zillow_url, headers=self.headers)
        response.status_code
        webpage = response.text
        soup = BeautifulSoup(webpage, 'html.parser')

        self.listings_address = [address.text.strip() for address in soup.find_all("address", {"data-test":"property-card-addr"})]
        self.listings_price = [price.text.replace("+", " ").replace("/"," ").split()[0] for price in soup.find_all("span", {"data-test":"property-card-price"})]
        self.listings_link = [link.get("href") for link in soup.find_all("a", {"data-test":"property-card-link"})]

        # listings = soup.find_all(name="div", class_="property-card-data")
        # for listing in listings:
        #     address = listing.find("address", {"data-test":"property-card-addr"}).text.strip()
        #     listings_address.append(address)

        #     price = listing.find("span", {"data-test":"property-card-price"}).text.replace("+", " ").replace("/"," ").split()[0]
        #     listings_prices.append(price)

        #     link = listing.find("a", {"data-test":"property-card-link"}).get("href")
        #     listings_link.append(link)


    def input_data_in_sheets(self):

        self.driver.get(self.form_url)

        for i in range(len(self.listings_address)):

            address_input = self.driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.click()
            time.sleep(2)
            address_input.send_keys(self.listings_address[i])

            time.sleep(2)
            price_input = self.driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input.click()
            time.sleep(2)
            price_input.send_keys(self.listings_price[i])

            time.sleep(2)
            link_input = self.driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input.click()
            time.sleep(2)
            link_input.send_keys(self.listings_link[i])

            time.sleep(2)
            submit_button = self.driver.find_element(By.XPATH, value='//span[contains(text(), "Submit")]')
            submit_button.click()

            time.sleep(3)
            submit_another_response_prompt = self.driver.find_element(By.XPATH, value='//a[contains(text(), "Submit another response")]')
            if submit_another_response_prompt:
                submit_another_response_prompt.click()
        
        self.driver.quit()

bot = ZillowRentalInfo()
bot.get_rental_info()
bot.input_data_in_sheets()
