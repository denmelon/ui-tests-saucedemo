# 🧪 SauceDemo UI Test Automation

UI tests for [SauceDemo](https://www.saucedemo.com) using Python, Selenium and pytest.
Features include parametrized login, filtering/sorting tests, screenshot capture on failures, and HTML reports.


## 🔧 Tech Stack

- Python 3.x
- Selenium WebDriver
- Pytest
- Pytest-HTML
- ChromeDriver

## 📁 Project Structure

```
ui-tests-saucedemo/
├── data/
│ └── login_data.json # Data for parametrized login tests
├── tests/
│ ├── conftest.py # Driver fixture and hooks
│ ├── test_login.py # Parametrized login tests
│ ├── test_add_to_cart.py # Test adding a product to cart
│ └── test_sorting.py # Test sorting functionality
├── screenshots/ # Auto screenshots upon failures
├── reports/
│ └── report.html # pytest-html report
├── .gitignore
├── requirements.txt
└── README.md
```

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

## 🚀 Setup

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

### 4. How to run tests


## 🧪 Running Tests

Generate HTML report with embedded screenshots:

```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

---

### 5. Tests and data info


## 🔍 Tests Overview

- `test_login.py` – Parametrized login tests using data from `data/login_data.json`, includes valid and invalid credentials.
- `test_add_to_cart.py` – Adds first product to cart and verifies it appears.
- `test_sorting.py` – Checks that "Price (low to high)" sorting works correctly.
```
## 📂 Login Data Structure

File: `data/login_data.json`

```json
[
  { "username": "standard_user", "password": "secret_sauce" },
  { "username": "locked_out_user", "password": "secret_sauce" },
  { "username": "problem_user", "password": "secret_sauce" }
]
```
Edit this to add new test credentials.


---


## 📸 Screenshots on Failure

If a test fails, a screenshot will be stored in `screenshots/`. These are automatically embedded in the HTML report.

## 🖼 Example Report

![Example report screenshot](screenshots/test_login.png)


### Requirements 
selenium
pytest
pytest-html

