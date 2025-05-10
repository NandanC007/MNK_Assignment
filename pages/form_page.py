from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "form_submit").click()

    def get_confirmation(self):
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "content"))
        ).text
