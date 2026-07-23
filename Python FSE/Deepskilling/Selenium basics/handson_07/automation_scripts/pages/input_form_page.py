from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InputFormPage(BasePage):

    URL = "https://www.testmuai.com/selenium-playground/input-form-demo/"

    NAME = (
        By.XPATH,
        "//input[@placeholder='Name']"
    )

    EMAIL = (
        By.XPATH,
        "//input[@placeholder='Email']"
    )

    PASSWORD = (
        By.XPATH,
        "//input[@placeholder='Password']"
    )

    COMPANY = (
        By.XPATH,
        "//input[@placeholder='Company']"
    )

    WEBSITE = (
        By.XPATH,
        "//input[@placeholder='Website']"
    )

    COUNTRY = (
        By.TAG_NAME,
        "select"
    )

    CITY = (
        By.XPATH,
        "//input[@placeholder='City']"
    )

    ADDRESS1 = (
        By.XPATH,
        "//input[@placeholder='Address 1']"
    )

    ADDRESS2 = (
        By.XPATH,
        "//input[@placeholder='Address 2']"
    )

    STATE = (
        By.XPATH,
        "//input[@placeholder='State']"
    )

    ZIPCODE = (
        By.XPATH,
        "//input[@placeholder='Zip code']"
    )


    SUBMIT = (
        By.XPATH,
        "//button[contains(text(),'Submit')]"
    )


    SUCCESS_MESSAGE = (
        By.CLASS_NAME,
        "success-msg"
    )


    def open_page(self):

        self.navigate_to(self.URL)



    def fill_form(self, name, email, phone, address):

        self.enter_text(
            self.NAME,
            name
        )

        self.enter_text(
            self.EMAIL,
            email
        )

        self.enter_text(
            self.PASSWORD,
            "Bak@123"
        )

        self.enter_text(
            self.COMPANY,
            "Cognizant"
        )

        self.enter_text(
            self.WEBSITE,
            "https://google.com"
        )


        country = self.wait_for_element(
            self.COUNTRY
        )

        Select(country).select_by_visible_text(
            "United States"
        )


        self.enter_text(
            self.CITY,
            "Chennai"
        )


        self.enter_text(
            self.ADDRESS1,
            address
        )


        self.enter_text(
            self.ADDRESS2,
            "Thoraipakkam"
        )


        self.enter_text(
            self.STATE,
            "Tamil Nadu"
        )


        self.enter_text(
            self.ZIPCODE,
            "600001"
        )



    def submit_form(self):

        self.click(
            self.SUBMIT
        )


    def get_success_message(self):

        return self.get_text(
            self.SUCCESS_MESSAGE
        )