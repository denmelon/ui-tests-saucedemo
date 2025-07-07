# 🧪 UI Test Automation: Saucedemo.com

This project is a beginner-friendly demo of UI test automation using Python and Selenium.  
It uses `pytest` for running tests and `pytest-html` for generating reports.

## 🔧 Tech Stack

- Python 3.x
- Selenium WebDriver
- Pytest
- Pytest-HTML
- ChromeDriver

## 📁 Project Structure

ui-tests-saucedemo/ 

TBU


## 🧪 Test: Add to Cart

This test does the following:

1. Opens [saucedemo.com](https://www.saucedemo.com)
2. Logs in as `standard_user`
3. Adds the first product to the cart
4. Navigates to the cart
5. Verifies that the item appears

### ✅ Assertion:

Check that product name is not empty in the cart.

### 📸 Screenshot:

![Cart Screenshot](screenshots/cart_page.png)

## 📊 HTML Report

To generate test report:

```bash
pytest tests/ --html=reports/report.html
```

The report is saved in the reports/ folder.

🚀 How to Run
1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run test:
```aiignore
pytest
```
