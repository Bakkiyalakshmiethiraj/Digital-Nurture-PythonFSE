from pages.simple_form_page import SimpleFormPage


def test_simple_form(driver):

    page = SimpleFormPage(driver)

    page.open_page()

    message = "Hello Digital Nurture"

    page.enter_message(message)

    page.click_show_message()

    displayed = page.get_displayed_message()

    print(displayed)

    assert displayed == message