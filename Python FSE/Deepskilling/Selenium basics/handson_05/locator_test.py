from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Implicit Wait
driver.implicitly_wait(10)

# --------------------------------------------------
# Step 32 & 33 - Simple Form Demo
# --------------------------------------------------

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# By.ID
element = driver.find_element(By.ID, "user-message")
print("✓ Found using ID")

# By.NAME
# Current LambdaTest page does not have a 'name' attribute for this input.
print("✗ By.NAME cannot be demonstrated because the input has no name attribute.")

# By.CLASS_NAME
element = driver.find_element(By.CLASS_NAME, "border")
print("✓ Found using CLASS_NAME")

# By.TAG_NAME
element = driver.find_element(By.TAG_NAME, "input")
print("✓ Found using TAG_NAME")

# Absolute XPath
element = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/main/div/section[2]/div/div/div/div[1]/div[2]/div/div[1]/input"
)
print("✓ Found using Absolute XPath")
# Relative XPath
element = driver.find_element(By.XPATH, "//input[@id='user-message']")
print("✓ Found using Relative XPath")

# CSS Selector by ID
element = driver.find_element(By.CSS_SELECTOR, "#user-message")
print("✓ CSS Selector using ID")

# CSS Selector by Attribute
element = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Please enter your Message']"
)
print("✓ CSS Selector using Attribute")

# CSS Selector using Parent > Child
try:
    element = driver.find_element(By.CSS_SELECTOR, "div > input")
    print("✓ CSS Selector Parent > Child")
except:
    print("✗ Parent > Child selector may differ in current page.")

# --------------------------------------------------
# Step 34 - Checkbox Demo
# --------------------------------------------------

driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")

# XPath using text()
try:
    label = driver.find_element(By.XPATH, "//label[text()='Option 1']")
    print("Label:", label.text)
except:
    print("Option 1 label not found using exact text().")

# XPath using contains()
labels = driver.find_elements(By.XPATH, "//label[contains(text(),'Option')]")

print("Labels found:")
for l in labels:
    print(l.text)

# --------------------------------------------------
# Step 35 - Locator Ranking
# --------------------------------------------------

"""
Locator Ranking (Best to Worst)

1. ID
2. NAME
3. CSS Selector
4. Relative XPath
5. CLASS_NAME
6. Absolute XPath

Reason:
- ID is unique and fastest.
- NAME is good if available.
- CSS Selector is fast and readable.
- Relative XPath is flexible.
- CLASS_NAME may match multiple elements.
- Absolute XPath is brittle and breaks if HTML changes.
"""

driver.quit()