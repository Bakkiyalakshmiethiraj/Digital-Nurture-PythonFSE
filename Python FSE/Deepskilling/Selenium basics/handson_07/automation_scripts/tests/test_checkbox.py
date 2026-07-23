from selenium.webdriver.common.by import By
import time

def test_checkbox(driver):

    driver.get("https://www.testmuai.com/selenium-playground/checkbox-demo")

    checkbox = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")

    print("Initially:", checkbox.is_selected())

    checkbox.click()
    time.sleep(2)

    print("After first click:", checkbox.is_selected())

    checkbox.click()
    time.sleep(2)

    print("After second click:", checkbox.is_selected())