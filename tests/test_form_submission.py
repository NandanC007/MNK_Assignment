from faker import Faker
from pages.form_page import FormPage

def test_form_submission(driver):
    fake = Faker()
    driver.get("https://the-internet.herokuapp.com/forgot_password")
    form = FormPage(driver)
    form.fill_form(fake.email())
    assert "Internal Server Error" in form.get_confirmation()
