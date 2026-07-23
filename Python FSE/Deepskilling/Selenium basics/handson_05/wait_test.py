import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.testmu.ai/selenium-playground/bootstrap-alert-messages-demo")

# -----------------------------------------------------
# Step 36 - Explicit Wait
# -----------------------------------------------------

success_button = driver.find_element(By.CSS_SELECTOR, ".btn-success-auto")
success_button.click()

alert = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
)

print("Step 36 Passed")
print("Alert Text:", alert.text)

assert "success" in alert.text.lower()

# -----------------------------------------------------
# Step 37 - time.sleep() vs Explicit Wait
# -----------------------------------------------------

driver.refresh()

start = time.time()

driver.find_element(By.CSS_SELECTOR, ".btn-success-auto").click()
time.sleep(3)

end = time.time()

print(f"time.sleep() Execution Time : {end-start:.2f} seconds")

driver.refresh()

start = time.time()

driver.find_element(By.CSS_SELECTOR, ".btn-success-auto").click()

WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-success"))
)

end = time.time()

print(f"Explicit Wait Execution Time : {end-start:.2f} seconds")

# Explicit Wait is faster because it waits only until the element appears.
# time.sleep() always waits the full specified duration.

# -----------------------------------------------------
# Step 38 - element_to_be_clickable()
# -----------------------------------------------------

driver.refresh()

button = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,".btn-success-auto"))
)

button.click()

print("Step 38 Passed - Button Clickable")

# visibility_of_element_located()
# -> Element is visible.

# element_to_be_clickable()
# -> Element is visible AND enabled.

# -----------------------------------------------------
# Step 39 - Fluent Wait
# -----------------------------------------------------

driver.refresh()

wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

button = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR,".btn-success-auto"))
)

print("Step 39 Passed - Fluent Wait Demonstrated")

driver.quit()