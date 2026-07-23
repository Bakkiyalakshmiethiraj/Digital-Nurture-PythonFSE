from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):

    URL = "https://www.testmuai.com/selenium-playground/select-dropdown-demo"

    DROPDOWN = (By.ID, "select-demo")


    def open_page(self):
        self.navigate_to(self.URL)


    def select_day(self, day):

        dropdown = Select(
            self.wait_for_element(self.DROPDOWN)
        )

        dropdown.select_by_visible_text(day)


    def get_selected_day(self):

        dropdown = Select(
            self.wait_for_element(self.DROPDOWN)
        )

        return dropdown.first_selected_option.text