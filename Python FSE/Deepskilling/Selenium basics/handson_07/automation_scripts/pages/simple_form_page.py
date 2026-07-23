from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SimpleFormPage(BasePage):

    URL = "https://www.testmuai.com/selenium-playground/simple-form-demo/"

    MESSAGE_INPUT = (By.ID, "user-message")
    SHOW_BUTTON = (By.ID, "showInput")
    MESSAGE = (By.ID, "message")

    def open_page(self):
        self.navigate_to(self.URL)

    def enter_message(self, message):
        self.enter_text(self.MESSAGE_INPUT, message)

    def click_show_message(self):
        self.click(self.SHOW_BUTTON)

    def get_displayed_message(self):
        return self.get_text(self.MESSAGE)