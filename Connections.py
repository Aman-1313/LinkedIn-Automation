import time,math,random,os
import utils,constants,config

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import prRed,prYellow,prGreen

from webdriver_manager.chrome import ChromeDriverManager

class Linkedin:
    def __init__(self):
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")
            prYellow("Trying to log in linkedin.")
        except Exception as e:
            prRed("Warning ChromeDriver"+ str(e))
        try:    
            self.driver.find_element("id","username").send_keys(config.email)
            time.sleep(5)
            self.driver.find_element("id","password").send_keys(config.password)
            time.sleep(5)
            self.driver.find_element("xpath",'//*[@id="organic-div"]/form/div[3]/button').click()
        except:
            prRed("Couldnt log in Linkedin.")
start = time.time()
Linkedin()
end = time.time()
prYellow("---Took: " + str(round((time.time() - start)/60)) + " minute(s).")