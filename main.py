import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from dlllllllllllllll import dev_controler
from datetime import datetime
#-------------------------------------------------------------------------------------------------------------------- 
current_time = datetime.now()
url_link = "https://www.freelancer.com/login"
url_recently = "https://www.freelancer.com/navigation/updates"
link_css_selector = "body > app-root > app-logged-in-shell > div > fl-container > div > div > ng-component > app-updates > app-updates-list > div.ng-tns-c194-22.ng-trigger.ng-trigger-slideInHorizontalAnimation.ng-star-inserted > fl-scrollable-content > app-project-item:nth-child(1) > app-feed-item > fl-button > a"
login_Btn = 'body > app-root > app-logged-out-shell > app-login-page > fl-container > fl-bit > app-login > app-credentials-form > form > app-login-signup-button > fl-button > button'
username = ""
password = ""
rec_link = None
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(url_link)
time.sleep(1)
email_input = driver.find_element(By.ID, 'emailOrUsernameInput')
email_input.send_keys(username)
time.sleep(1)
password_input = driver.find_element(By.ID, 'passwordInput')
password_input.send_keys(password)
login_button = driver.find_element(By.CSS_SELECTOR, login_Btn)
login_button.click()
time.sleep(5)
driver.get(url_recently)
time.sleep(5)
for i in range (1000):
    print(".")
print(f"username = {username}")
print(f"password = {password[:4]}...")
run  = True
while run:
        try:
            target_element = driver.find_element(By.CSS_SELECTOR, link_css_selector)
            link = target_element.get_attribute("href")
        except:
            response = requests.get(url_recently)
            soup = BeautifulSoup(response.text, 'html.parser')
            target_element  = soup.select_one(link_css_selector)
            link = rec_link
            print("hier is faild ")
            print(target_element.contents)
        
        if link == rec_link :
            continue
        else:
            if target_element:
                print("----------------------------------------------->")
                rec_link = link
                print(f"URL >> {link}")
                status = dev_controler.see_discrib(link,0)
                print(f"status func = {status}")
                print("------------------------------------------->>>>")
            else:
                print("NO")