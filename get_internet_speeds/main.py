from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""gets your upload and download speeds """
class InternetSpeeds:
    def __init__(self):
        self.firefox_options = webdriver.FirefoxOptions()
        self.firefox_options.set_preference('detach', True)
        self.driver = webdriver.Firefox(options=self.firefox_options)
        self.up: int
        self.down: int
        
    def get_internet_speed(self):
        self.driver.get(url='https://speedtest.net')
        start_test_button = self.driver.find_element(By.CLASS_NAME, value='start-text')
        start_test_button.click()
        time.sleep(50)

        self.down = self.driver.find_element(By.CLASS_NAME, value='download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, value='upload-speed').text
        
        self.driver.quit()
        return f'DOWN: {self.down}Mbps | UP: {self.up}Mbps '

bot = InternetSpeeds()
print(bot.get_internet_speed())