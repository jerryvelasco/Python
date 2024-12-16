from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

IG_USERNAME = 'ENTER YOUR INSTAGRAM USERNAME'
IG_PW = 'ENTER YOUR INSTAGRAM PASSWORD'

"""gets hold of all the accounts being followed and then unfollows all of them"""
class InstaFollower:
    def __init__(self):
        self.firefox_options = webdriver.FirefoxOptions()
        self.firefox_options.set_preference('detach', True)
        self.driver = webdriver.Firefox(options=self.firefox_options)
        self.action = ActionChains(self.driver)


    """login using credentials"""
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)

        username = self.driver.find_element(By.CSS_SELECTOR, value='input[name="username"]')
        username.click()
        time.sleep(5)
        username.send_keys(IG_USERNAME)

        pw = self.driver.find_element(By.CSS_SELECTOR, value='input[name="password"]')
        pw.click()
        time.sleep(5)
        pw.send_keys(IG_PW, Keys.ENTER)
        
        time.sleep(5)
        save_login_info_prompt = self.driver.find_element(By.CSS_SELECTOR, value='div[role="button"]')
        if save_login_info_prompt:
            save_login_info_prompt.click()

        time.sleep(5)
        turn_on_notifications_prompt = self.driver.find_element(By.XPATH, value='//*[contains(text(), "Not Now")]')
        if turn_on_notifications_prompt:
            turn_on_notifications_prompt.click()


    """find all of the accounts being followed"""
    def find_followers(self, scroll_limit):
        profile = self.driver.find_element(By.CSS_SELECTOR, value=f'a[href="/{IG_USERNAME}/"]')
        profile.click()

        time.sleep(5)
        following = self.driver.find_element(By.CSS_SELECTOR, value=f'a[href="/{IG_USERNAME}/following/"]')
        following.click()

        time.sleep(5)

        followers_popup_list = self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]")

        for _ in range(scroll_limit):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', followers_popup_list)
            time.sleep(2)


    """based on all of the accounts being followed, unfollow them"""
    def unfollow_everyone(self):
        time.sleep(5)

        following_button_list = self.driver.find_elements(By.CSS_SELECTOR, value='button[type="button"]')

        time.sleep(2)
        for users in following_button_list:

            if users.text == "Following":
                users.click()
                time.sleep(5)

                unfollow_confirmation = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Unfollow')]")
                unfollow_confirmation.click()
                time.sleep(5)

                try_again_later_prompt = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'OK')]")
                if try_again_later_prompt:
                    try_again_later_prompt.click()
                    time.sleep(5)

bot = InstaFollower()
bot.login()
bot.find_followers(scroll_limit=2)
bot.unfollow_everyone()
