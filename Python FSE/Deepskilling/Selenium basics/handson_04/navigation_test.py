from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Implicit Wait
driver.implicitly_wait(10)

# Open Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

# Click on "Simple Form Demo"
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Verify URL
assert "simple-form-demo" in driver.current_url

print("Current URL:", driver.current_url)

# Go back to previous page
driver.back()

# Open a new browser tab
driver.execute_script('window.open("https://www.google.com");')

# List all open tabs
print("Window Handles:", driver.window_handles)

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Print Google page title
print("Google Title:", driver.title)

# Switch back to the original tab
driver.switch_to.window(driver.window_handles[0])

# Take screenshot
driver.save_screenshot("playground_screenshot.png")
print("Screenshot saved successfully.")

# Get current window size
print("Window Size:", driver.get_window_size())

# Set new window size
driver.set_window_size(1280, 800)

# Consistent window size helps maintain stable UI automation
# by ensuring elements appear in the same layout during every test.

driver.quit()