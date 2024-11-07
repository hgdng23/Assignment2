import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_edit_info():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='email' and @placeholder='E-Mail Address']").send_keys(
        "dang@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("12345")
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Edit Account").click()
    time.sleep(2)
    driver.find_element(By.ID, "input-firstname").clear()
    driver.find_element(By.ID, "input-firstname").send_keys("Dao")
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    success_message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    assert "Success: Your account has been successfully updated." in success_message, "Thông báo thành công không đúng!"
    driver.quit()

def test_edit_info_emty_firtsname():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='email' and @placeholder='E-Mail Address']").send_keys(
        "dang@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("12345")
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Edit Account").click()
    time.sleep(2)
    driver.find_element(By.ID, "input-firstname").clear()
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH, "//div[@id='error-firstname']").text
    assert "First Name must be between 1 and 32 characters!" in error_message, "Thông báo lỗi không đúng!"
    driver.quit()



