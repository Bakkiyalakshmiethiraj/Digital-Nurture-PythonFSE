from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Test Case 1 - Verify Page Title
def test_page_title(driver):

    driver.get("https://www.testmuai.com/selenium-playground/")

    print("Page Title:", driver.title)

    assert driver.title != ""


# Test Case 2 - Verify Heading is Displayed
def test_heading_present(driver):

    driver.get("https://www.testmuai.com/selenium-playground/")

    heading = driver.find_element(By.TAG_NAME, "h1")

    print("Heading:", heading.text)

    assert heading.is_displayed()


# Test Case 3 - Verify Checkbox Selection
def test_checkbox_demo(driver):

    driver.get("https://www.testmuai.com/selenium-playground/checkbox-demo")

    wait = WebDriverWait(driver, 10)

    # Locate the first checkbox under "Single Checkbox Demo"
    checkbox = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//input[@type='checkbox'])[1]")
        )
    )

    # Click the checkbox
    checkbox.click()

    # Verify checkbox is selected
    assert checkbox.is_selected()

    print("✅ Checkbox Selected")

    # Click again
    checkbox.click()

    # Verify checkbox is deselected
    assert not checkbox.is_selected()

    print("✅ Checkbox Deselected")