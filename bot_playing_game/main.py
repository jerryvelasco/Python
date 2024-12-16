from selenium import webdriver
from selenium.webdriver.common.by import By
import time

firefox_options = webdriver.FirefoxOptions()
firefox_options.set_preference('detach', True)

driver = webdriver.Firefox(options=firefox_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

#controls timing
five_second_interval = time.time() + 5
game_over_timer = time.time() + 60*2

#selects the cookies image
cookie = driver.find_element(By.ID, value="cookie")

#selects all of the upgrade options 
upgrade_store_data = driver.find_elements(By.CSS_SELECTOR, value='#store b')

#splits all of the upgrade store options 
store_data_split =  [upgrades.text.split() for upgrades in upgrade_store_data]
prices = {}

#turns the upgrade options into a dict
for options in range(len(store_data_split)-1):
    prices[options] = { 
        'name': store_data_split[options][0], 
        'cost': int(store_data_split[options][-1].replace(',','')) 
    }

while True:

    cookie.click()

    #check every 5 secs 
    if time.time() > five_second_interval:

        #add 5 seconds to time
        five_second_interval = time.time() + 5

        affordable_upgrades = {}

        cookie_count = int(driver.find_element(By.ID, value='money').text.replace(',',''))

        #checks what upgrades we can do based on how many cookies we have and adds them to the affordable dict
        for items in range(len(prices)):
            if cookie_count > prices[items]['cost']:
                affordable_upgrades[items] = prices[items]
        
        #finds the index of the highest value in the afforable dict and then clicks it based on the id
        highest_affordable_index = max(affordable_upgrades)
        hightest_affordable_name = affordable_upgrades[highest_affordable_index]['name']
        highest_affordable_option = driver.find_element(By.ID, value=f'buy{hightest_affordable_name}')
        highest_affordable_option.click()
        
    #controls when the automation ends 
    if time.time() > game_over_timer:
        cookies_per_sec = driver.find_element(By.ID, value='cps').text
        print(cookies_per_sec)
        break
        
driver.quit()
        
