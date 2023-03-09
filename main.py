from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.google.com"

f_options = webdriver.FirefoxOptions()
f_options.add_argument('-headless')
driver = webdriver.Firefox(options=f_options)
driver.get(url)

searchbox = driver.find_element(By.NAME,"q")
searchbox.send_keys("Python")
searchbox.send_keys(Keys.ENTER)

try:
    python_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//a[@href='https://www.python.org/']"))
        )
finally:
    python_link.send_keys(Keys.ENTER)

try:
    WebDriverWait(driver, 10).until(
                EC.title_contains("Welcome to Python.org")
            )
finally:
    assert driver.title == "Welcome to Python.org", print("Error, title is: {}", driver.title)
    driver.close()