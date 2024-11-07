import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_register_user():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='firstname' and @placeholder='First Name']").send_keys("Hoang")
    driver.find_element(By.XPATH, "//input[@name='lastname' and @placeholder='Last Name']").send_keys("Dang")
    driver.find_element(By.XPATH, "//input[@name='email' and @placeholder='E-Mail']").send_keys("dang1@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("12345")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    success_message = driver.find_element(By.XPATH, "//h1[text()='Your Account Has Been Created!']")
    assert success_message.is_displayed(), "Dòng text xác nhận không được hiển thị."
    driver.quit()

def test_register_emty_email():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='firstname' and @placeholder='First Name']").send_keys("Hoang")
    driver.find_element(By.XPATH, "//input[@name='lastname' and @placeholder='Last Name']").send_keys("Dang")
    driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("12345")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    error = driver.find_element(By.ID, "error-email").text
    assert "E-Mail Address does not appear to be valid!" in error
    driver.quit()

def test_register_short_password():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='firstname' and @placeholder='First Name']").send_keys("Hoang")
    driver.find_element(By.XPATH, "//input[@name='lastname' and @placeholder='Last Name']").send_keys("Dang")
    driver.find_element(By.XPATH, "//input[@name='email' and @placeholder='E-Mail']").send_keys("dang10@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("123")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    error = driver.find_element(By.ID, "error-password").text
    assert "Password must be between 4 and 20 characters!" in error
    driver.quit()

def test_agree_privacy_policy():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='firstname' and @placeholder='First Name']").send_keys("Hoang")
    driver.find_element(By.XPATH, "//input[@name='lastname' and @placeholder='Last Name']").send_keys("Dang")
    driver.find_element(By.XPATH, "//input[@name='email' and @placeholder='E-Mail']").send_keys("dang10@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("12345")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    error_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='alert']")))
    assert "Warning: You must agree to the Privacy Policy!" in error_alert.get_attribute("innerText")
    driver.quit()

