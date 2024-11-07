import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_fill_in_shipping_address():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='email' and @placeholder='E-Mail Address']").send_keys("dang123@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("12345")
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/header/div/div/div[1]/div/a/img").click()
    driver.find_element(By.XPATH,
    "//img[@src='http://localhost/opencart-4.0.2.3/upload/image/cache/catalog/demo/iphone_1-200x200.jpg']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary btn-lg btn-block']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//span[@class='d-none d-md-inline' and text()='Checkout']").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-shipping-new").click()
    driver.find_element(By.ID, "input-shipping-firstname").send_keys("Hoang")
    driver.find_element(By.ID, "input-shipping-lastname").send_keys("Dang")
    driver.find_element(By.ID, "input-shipping-company").send_keys("SGU")
    driver.find_element(By.ID, "input-shipping-address-1").send_keys("123 Đường ADV")
    driver.find_element(By.ID, "input-shipping-address-2").send_keys("105 Đường BHTQ")
    driver.find_element(By.ID, "input-shipping-city").send_keys("TpHCM")
    driver.find_element(By.ID, "input-shipping-postcode").send_keys("100000")
    time.sleep(1)
    driver.find_element(By.ID, "input-shipping-country").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//option[text()='Viet Nam']").click()
    time.sleep(1)
    zone_dropdown = driver.find_element(By.ID, "input-shipping-zone")
    driver.execute_script("arguments[0].scrollIntoView();", zone_dropdown)
    time.sleep(1)
    driver.find_element(By.ID, "input-shipping-zone").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//option[text()='Ho Chi Minh City']").click()
    driver.find_element(By.XPATH, "//button[@type='submit' and @id='button-shipping-address']").click()
    time.sleep(5)
    success_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert alert-success')]")))
    assert "Success: You have changed shipping address!" in success_alert.get_attribute("innerText")
    driver.quit()

def test_error_fill_in_shipping_address():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='email' and @placeholder='E-Mail Address']").send_keys("dang123@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("12345")
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/header/div/div/div[1]/div/a/img").click()
    driver.find_element(By.XPATH,
    "//img[@src='http://localhost/opencart-4.0.2.3/upload/image/cache/catalog/demo/iphone_1-200x200.jpg']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary btn-lg btn-block']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//span[@class='d-none d-md-inline' and text()='Checkout']").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-shipping-new").click()
    driver.find_element(By.ID, "input-shipping-firstname").send_keys("Hoang")
    driver.find_element(By.ID, "input-shipping-lastname").send_keys("Dang")
    driver.find_element(By.ID, "input-shipping-company").send_keys("SGU")
    driver.find_element(By.ID, "input-shipping-address-1").send_keys("123 Đường ADV")
    driver.find_element(By.ID, "input-shipping-address-2").send_keys("105 Đường BHTQ")
    driver.find_element(By.ID, "input-shipping-city").send_keys("TpHCM")
    driver.find_element(By.ID, "input-shipping-postcode").send_keys("100000")
    time.sleep(1)
    driver.find_element(By.ID, "input-shipping-country").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//option[text()='Viet Nam']").click()
    time.sleep(1)
    zone_dropdown = driver.find_element(By.ID, "input-shipping-zone")
    driver.execute_script("arguments[0].scrollIntoView();", zone_dropdown)
    time.sleep(1)
    driver.find_element(By.ID, "input-shipping-zone").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@type='submit' and @id='button-shipping-address']").click()
    time.sleep(5)
    error = driver.find_element(By.ID, "error-shipping-zone").text
    assert "Please select a region / state!" in error
    driver.quit()

def test_check_out_confirm ():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='email' and @placeholder='E-Mail Address']").send_keys(
        "dang123@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("12345")
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/header/div/div/div[1]/div/a/img").click()
    driver.find_element(By.XPATH,
                        "//img[@src='http://localhost/opencart-4.0.2.3/upload/image/cache/catalog/demo/iphone_1-200x200.jpg']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary btn-lg btn-block']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//span[@class='d-none d-md-inline' and text()='Checkout']").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-shipping-existing").click()
    dropdown = driver.find_element(By.ID, "input-shipping-address")
    select = Select(dropdown)
    select.select_by_value("16")
    time.sleep(3)
    driver.find_element(By.ID, "button-shipping-methods").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-shipping-method-flat-flat").click()
    driver.find_element(By.ID, "button-shipping-method").click()
    driver.find_element(By.ID, "button-payment-methods").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-payment-method-cod-cod").click()
    driver.find_element(By.ID, "button-payment-method").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        confirm_order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "button-confirm")))
        confirm_order_button.click()
    except Exception as e:
        print("Nút 'Confirm Order' không thể nhấp được:", e)
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Your order has been placed!']")))
    assert success_message.is_displayed(), "Dòng text xác nhận không được hiển thị."
    driver.quit()