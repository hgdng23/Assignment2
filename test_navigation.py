import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navigation():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.CSS_SELECTOR, 'i.fa-solid.fa-phone').click()
    time.sleep(3)
    assert "http://localhost/opencart-4.0.2.3/upload/index.php?route=information/contact&language=en-gb" in driver.current_url
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)
    assert "http://localhost/opencart-4.0.2.3/upload/index.php?route=account/login&language=en-gb" in driver.current_url
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(3)
    assert "http://localhost/opencart-4.0.2.3/upload/index.php?route=account/register&language=en-gb" in driver.current_url
    driver.find_element(By.XPATH, "//span[@class='d-none d-md-inline' and text()='Checkout']").click()
    time.sleep(3)
    assert "http://localhost/opencart-4.0.2.3/upload/index.php?route=checkout/cart&language=en-gb" in driver.current_url
    driver.quit()


