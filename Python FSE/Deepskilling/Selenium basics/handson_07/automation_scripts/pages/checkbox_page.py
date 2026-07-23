from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckboxPage(BasePage):

    URL = "https://www.testmuai.com/selenium-playground/checkbox-demo"

    CHECKBOX = (By.XPATH, "(//input[@type='checkbox'])[1]")

    def open_page(self):
        self.navigate_to(self.URL)

    def click_checkbox(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKBOX)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            checkbox
        )

        checkbox.click()

    def is_checkbox_selected(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CHECKBOX)
        )
        return checkbox.is_selected()