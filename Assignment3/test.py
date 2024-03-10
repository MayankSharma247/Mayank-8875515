# Importing required libraries
from selenium import webdriver
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the LinkedIn homepage
driver.get("https://linkedin.com/")
time.sleep(2)

# Click on the Learning link
learning_link = driver.find_element("xpath", "/html/body/nav/ul/li[3]/a")
learning_link.click()
time.sleep(3)

# Click on the Business link
business_link = driver.find_element("xpath", "/html/body/div/div[1]/div/a[1]")
business_link.click()
time.sleep(3)

# Click on the product link
product_link = driver.find_element("xpath", "/html/body/section[1]/div/header/div[1]/div/nav/ul[1]/li[1]/a")
product_link.click()
time.sleep(3)

# Click on the contact sales link
contact_sales_link = driver.find_element("xpath", "/html/body/section[1]/div/header/div[1]/div/nav/ul[2]/li/a")
contact_sales_link.click()
time.sleep(3)

# Closing the webdriver
driver.close()
