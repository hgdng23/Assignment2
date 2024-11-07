from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_contact():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//i[@class='fa-solid fa-phone']").click()
    time.sleep(2)
    driver.find_element(By.ID, "input-name").send_keys("Dang")
    driver.find_element(By.ID, "input-email").send_keys("dang@gmail.com")
    driver.find_element(By.ID, "input-enquiry").send_keys("1234567890")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    success_message = driver.find_element(By.XPATH, "//p[text()='Your enquiry has been successfully sent to the store owner!']")
    assert success_message.is_displayed(), "Dòng text xác nhận không được hiển thị."
    driver.quit()

def test_contact_invalid_email():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//i[@class='fa-solid fa-phone']").click()
    time.sleep(2)
    driver.find_element(By.ID, "input-name").send_keys("Dang")
    driver.find_element(By.ID, "input-email").send_keys("dang1gmail.com")
    driver.find_element(By.ID, "input-enquiry").send_keys("1234567890")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(5)
    error = driver.find_element(By.ID, "error-email").text
    assert "E-Mail Address does not appear to be valid!" in error
    driver.quit()
