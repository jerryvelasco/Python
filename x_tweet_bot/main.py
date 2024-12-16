from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TWITTER_PW = "ENTER YOUR PASSWORD"
TWITTER_EMAIL = "ENTER YOUR EMAIL"

"""post tweet to twitter/x account using provided credentials"""
class TwitterBot:
    def __init__(self):
        self.firefox_options = webdriver.FirefoxOptions()
        self.firefox_options.set_preference('detach', True)
        self.driver = webdriver.Firefox(options=self.firefox_options)
        
        self.up: int
        self.down: int

    def post_tweet(self):
        self.driver.get(url='https://x.com/login')
        time.sleep(2)
        email = self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
        email.send_keys(TWITTER_EMAIL, Keys.ENTER)

        input("Complete Captcha then press Enter") 

        time.sleep(5)
        password = self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
        password.send_keys(TWITTER_PW, Keys.ENTER)

        time.sleep(10)
        tweet_input_box = self.driver.find_element(By.CLASS_NAME, value='DraftEditor-root')
        tweet_input_box.click()

        time.sleep(5)
        # write_tweet = self.driver.find_element(By.XPATH, value="*//*[@contenteditable='true']")
        write_tweet = self.driver.find_element(By.CSS_SELECTOR, value="div[contenteditable='true']")
        tweet = input('enter a tweet you want posted: ')
        write_tweet.send_keys(tweet)

        time.sleep(5)
        post_tweet = self.driver.find_element(By.CSS_SELECTOR, value='button[data-testid="tweetButtonInline"]')
        post_tweet.click()

bot = TwitterBot()
bot.post_tweet()
