import pytest
import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def load_login_data():
    import os, json
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "..", "data", "login_data.json")
    json_path = os.path.abspath(json_path)

    with open(json_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
        return [(entry["username"], entry["password"]) for entry in raw_data]


@pytest.mark.parametrize("username,password", load_login_data())
def test_login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    if username == "locked_out_user":
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        assert error.is_displayed()
    else:
        assert "inventory" in driver.current_url
