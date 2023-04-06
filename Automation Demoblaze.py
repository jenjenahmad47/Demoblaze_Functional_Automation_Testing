from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time  
import string    
import random

print("Test case now started")

options = webdriver.ChromeOptions()
options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Opens Demoblaze page
url=driver.get("https://www.demoblaze.com/index.html")
time.sleep(10)

# Generate random string for username
S = 10 
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    

# Sign Up
signup=driver.find_element(By.LINK_TEXT, "Sign up").click()
time.sleep(4)
signup_username=driver.find_element(By.ID, "sign-username").send_keys(ran)
time.sleep(4)
signup_password=driver.find_element(By.ID, "sign-password").send_keys("test123")
time.sleep(4)
click_signup=driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[2]").click()
time.sleep(4)
driver.switch_to.alert.accept()
time.sleep(6)

# Log in
login=driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(4)
login_username=driver.find_element(By.ID, "loginusername").send_keys("connorkenway1477")
time.sleep(4)
login_password=driver.find_element(By.ID, "loginpassword").send_keys("test123")
time.sleep(4)
click_login=driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[3]").click()
time.sleep(6)

# Cart
cart=driver.find_element(By.ID, "cartur").click()
time.sleep(4)
add_cart=driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(4)
cart_name=driver.find_element(By.ID, "name").send_keys("Connor Kenway")
time.sleep(4)
cart_country=driver.find_element(By.ID, "country").send_keys("Arkansas, United States")
time.sleep(4)
cart_city=driver.find_element(By.ID, "city").send_keys("Arkadelphia")
time.sleep(4)
cart_card=driver.find_element(By.ID, "card").send_keys("036244897")
time.sleep(4)
cart_month=driver.find_element(By.ID, "month").send_keys("April")
time.sleep(4)
cart_year=driver.find_element(By.ID, "year").send_keys("2023")
time.sleep(4)
purchase_cart=driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[3]").click()
time.sleep(4)
ok_cart=driver.find_element(By.XPATH, "//button[contains(@class,'confirm btn')]").click()
time.sleep(6)

# About us
about_us=driver.find_element(By.LINK_TEXT, "About us").click()
time.sleep(6)
close_about_us=driver.find_element(By.XPATH, "//div[@id='videoModal']/div[1]/div[1]/div[3]/button[1]").click()
time.sleep(6)

# Contact
contact=driver.find_element(By.LINK_TEXT, "Contact").click()
time.sleep(4)
contact_email=driver.find_element(By.XPATH, "(//input[@class='form-control'])[1]").send_keys("connorkenway1477@hotmail.com")
time.sleep(2)
contact_name=driver.find_element(By.XPATH, "(//input[@class='form-control'])[2]").send_keys("Connor Kenway")
time.sleep(2)
contact_message=driver.find_element(By.ID, "message-text").send_keys("In the name of liberty, I will fight the enemy regardless of their allegiance.")
time.sleep(4)
send_message=driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
time.sleep(4)
driver.switch_to.alert.accept()
time.sleep(6)

# Sidebar
monitors=driver.find_element(By.LINK_TEXT, "Monitors").click()
time.sleep(4)
phones=driver.find_element(By.LINK_TEXT, "Phones").click()
time.sleep(4)
laptops=driver.find_element(By.LINK_TEXT, "Laptops").click()
time.sleep(4)

# Home
home=driver.find_element(By.XPATH, "//a[@class='nav-link']").click()
time.sleep(4)

# Log out
logout=driver.find_element(By.LINK_TEXT, "Log out").click()
time.sleep(6)

# Close the Chrome
driver.close()

print("\nTest case successfully completed")