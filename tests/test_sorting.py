from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_sort_products(driver):
    driver.get("https://www.saucedemo.com/")

    # Log in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url, "Login failed"

    # Sort products by price (low to high)
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Price (low to high)")

    # Verify sorting
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(product.text.replace("$", "")) for product in products]

    assert prices == sorted(prices), "Products are not sorted by price (low to high)"