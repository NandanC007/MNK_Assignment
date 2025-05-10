import json
import pytest
from pages.login_page import LoginPage

def test_login_success(driver):
    with open("config/config.json") as f:
        config = json.load(f)

    driver.get(config["url"])
    login = LoginPage(driver)
    login.login(config["username"], config["password"])
    assert login.is_login_successful()
