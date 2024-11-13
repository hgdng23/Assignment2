import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='email' and @placeholder='E-Mail Address']").send_keys("dang@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("12345")
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    assert "http://localhost/opencart-4.0.2.3/upload/index.php?route=account/account&language=en-gb&customer_token=" in driver.current_url
    driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='email' and @placeholder='E-Mail Address']").send_keys("dang@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("1")
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    error_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='alert']")))
    assert "Warning: No match for E-Mail Address and/or Password." in error_alert.get_attribute("innerText")
    driver.quit()

def test_empty_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    error_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='alert']")))
    assert "Warning: No match for E-Mail Address and/or Password." in error_alert.get_attribute("innerText")
    driver.quit()


