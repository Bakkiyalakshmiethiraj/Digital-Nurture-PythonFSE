from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
options = Options()
options.add_argument("--headless")

# Launch Chrome browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Implicit wait applies to all elements globally.
# It is less flexible because every element lookup waits up to the specified time.
# Explicit waits are preferred since they wait only for specific elements or conditions.
driver.implicitly_wait(10)

# Open LambdaTest Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

# Print page title
print("Page Title:", driver.title)

# Close browser
driver.quit()