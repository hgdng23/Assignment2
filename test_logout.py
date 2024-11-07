import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_logout():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='email' and @placeholder='E-Mail Address']").send_keys("dang@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("12345")
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[5]/a").click()
    time.sleep(2)
    assert "http://localhost/opencart-4.0.2.3/upload/index.php?route=account/logout&language=en-gb" in driver.current_url
    driver.quit()
