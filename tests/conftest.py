# test/conftest.py
import os.path

import pytest
import pytest_html.extras
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# Pytest hook: save screenshot if test failed
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            filename = f"{item.name}.png"
            path = os.path.join(screenshots_dir, filename)
            driver.save_screenshot(path)
            # print(f"\n📸 Screenshot saved to: {path}")
            if hasattr(result, 'extra'):
                result.extra.append(pytest_html.extras.image(path))
            else:
                result.extra = [pytest_html.extras.image(path)]

def pytest_html_report_title(report):
    report.title = "UI Automation Report: SauceDemo"

def pytest_html_results_table_row(report, cells):
    if report.when == "call" and hasattr(report,"extra"):
        for extra in report.extra:
            if extra['content_type'] == 'image/png':
                html = f'<img src="{extra["filename"]}" width="200"/>'
                cells.insert(1, html)