from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_search():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='text' and @name='search']").send_keys("mac")
    driver.find_element(By.XPATH, "//input[@type='text' and @name='search']").send_keys(Keys.ENTER)
    time.sleep(5)
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#product-list .product-thumb")))
    product_elements = driver.find_elements(By.CSS_SELECTOR, "#product-list .product-thumb h4 a")
    product_names = [product.text.lower() for product in product_elements]
    for product_name in product_names:
        assert "mac" in product_name, f"Kết quả '{product_name}' không chứa từ khóa 'mac'."
    driver.quit()

def test_special_character_search():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='text' and @name='search']").send_keys("!@#$%^&")
    driver.find_element(By.XPATH, "//input[@type='text' and @name='search']").send_keys(Keys.ENTER)
    time.sleep(5)
    no_result_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(), 'There is no product that matches the search criteria.')]")))
    assert no_result_message.text == ("There is no product that matches the search criteria.")
    driver.quit()


def test_search_02():
    driver = webdriver.Chrome()
    driver.get("http://localhost/opencart-4.0.2.3/upload/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='text' and @name='search']").send_keys("samsung mac")
    driver.find_element(By.XPATH, "//input[@type='text' and @name='search']").send_keys(Keys.ENTER)
    time.sleep(2)
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#product-list .product-thumb")))
    product_elements = driver.find_elements(By.CSS_SELECTOR, "#product-list .product-thumb h4 a")
    product_names = [product.text.lower() for product in product_elements]
    for product_name in product_names:
        assert "samsung" in product_name or "mac" in product_name, \
            f"Kết quả '{product_name}' không chứa 'samsung' hoặc 'mac'."
    driver.quit()