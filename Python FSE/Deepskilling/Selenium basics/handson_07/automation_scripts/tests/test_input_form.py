from pages.input_form_page import InputFormPage


def test_input_form_submit(driver):

    page = InputFormPage(driver)

    page.open_page()

    page.fill_form(
        "Bakkyalakshmi E",
        "bakkyalakshmi@gmail.com",
        "6374527209",
        "Chennai"
    )

    page.submit_form()

    message = page.get_success_message()

    print(message)

    assert "Thanks for contacting us" in message