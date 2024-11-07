import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//img[@src='http://localhost/opencart-4.0.2.3/upload/image/cache/catalog/demo/macbook_1-200x200.jpg']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary btn-lg btn-block']").click()
    time.sleep(2)
    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-toggle='dropdown' and contains(text(), 'item(s)')]")))
    cart_text = cart_button.text
    assert "1 item(s)" in cart_text
    driver.quit()

def test_add_multiple_to_cart():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//img[@src='http://localhost/opencart-4.0.2.3/upload/image/cache/catalog/demo/macbook_1-200x200.jpg']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='input-quantity']").clear()
    driver.find_element(By.XPATH, "//input[@id='input-quantity']").send_keys("5")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary btn-lg btn-block']").click()
    time.sleep(2)
    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-toggle='dropdown' and contains(text(), 'item(s)')]")))
    cart_text = cart_button.text
    assert "5 item(s)" in cart_text
    driver.quit()

def test_increase_product_quantity():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//img[@src='http://localhost/opencart-4.0.2.3/upload/image/cache/catalog/demo/macbook_1-200x200.jpg']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-primary btn-lg btn-block']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[4]/a/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='quantity']").clear()
    driver.find_element(By.XPATH, "//input[@name='quantity']").send_keys("15")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr/td[4]/form/div/button[1]").click()
    time.sleep(2)
    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-toggle='dropdown' and contains(text(), 'item(s)')]")))
    cart_text = cart_button.text
    assert "15 item(s)" in cart_text
    driver.quit()

def test_add_more_products_to_cart():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[@href='http://localhost/opencart-4.0.2.3/upload/index.php?route=product/category&language=en-gb&path=24']").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 200);")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[1]/div/div[2]/form/div/button[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[2]/div/div[2]/form/div/button[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[3]/div/div[2]/form/div/button[1]").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='Shopping Cart']").click()
    time.sleep(2)
    driver.quit()

