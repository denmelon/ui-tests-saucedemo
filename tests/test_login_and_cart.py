from selenium.webdriver.common.by import By

def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url, "Login failed"

    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link")

    item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_name != "", "Item is not found in the cart"