from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = 'ENTER YOUR LINKEDIN USERNAME '
PASSWORD = 'ENTER YOUR LINKEDIN PASSWORD'
LINK_FROM_SEARCHING_JOBS ='https://www.linkedin.com/jobs/search/?currentJobId=3980072855&f_AL=true&geoId=103644278&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R'
"https://www.linkedin.com/jobs/search/?currentJobId=3921696513&f_AL=true&geoId=105080838&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true&sortBy=R"
        
firefox_options = webdriver.FirefoxOptions()
firefox_options.set_preference('detach', True)

driver = webdriver.Firefox(options=firefox_options)
driver.get(url=LINK_FROM_SEARCHING_JOBS)

#logins with credentials 
time.sleep(2)
initial_sign_in_button = driver.find_element(By.CLASS_NAME, value='nav__button-secondary')
initial_sign_in_button.click()

time.sleep(2)
username_input_box = driver.find_element(By.ID, value='username')
username_input_box.send_keys(USERNAME)
password_input_box = driver.find_element(By.ID, value='password')
password_input_box.send_keys(PASSWORD)

signin_button = driver.find_element(By.CLASS_NAME, value='from__button--floating')
signin_button.click()

#break for captcha to be completed manually 
input('press enter after completing captcha!')

time.sleep(5)

#grabs available jobs listed 
jobs_list = driver.find_elements(By.CLASS_NAME, value='job-card-container--clickable')

for jobs in jobs_list:
    jobs.click()

    # time.sleep(3)

    #checks if jobs has been saved already 
    save_button = driver.find_element(By.CSS_SELECTOR, value='button.jobs-save-button')
    if save_button.text.split()[0] == 'Saved':
        print('job was already saved')
    else:
        save_button.click()
        print('saved job successfully')
        continue

    # time.sleep(2)
    




