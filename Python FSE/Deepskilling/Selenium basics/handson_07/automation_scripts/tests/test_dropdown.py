from pages.dropdown_page import DropdownPage


def test_dropdown_selection(driver):

    page = DropdownPage(driver)

    page.open_page()

    page.select_day("Wednesday")

    selected = page.get_selected_day()

    print("Selected:",
          selected)

    assert selected == "Wednesday"