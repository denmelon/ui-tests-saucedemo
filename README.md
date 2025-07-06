# 🧪 UI Test Automation: Login Test for saucedemo.com

This is a simple UI automation project using **Python** and **Selenium WebDriver** to test the login functionality of [saucedemo.com](https://www.saucedemo.com), a demo e-commerce website provided by Sauce Labs.

## ✅ What is tested
- Opening the site in Chrome browser
- Entering valid credentials (`standard_user` / `secret_sauce`)
- Clicking the login button
- Verifying successful login by checking the URL

## 🛠 Technologies Used
- Python 3.x
- Selenium WebDriver
- Jupyter Notebook (via Anaconda)
- Google Chrome + chromedriver

## 🔧 Setup Instructions

### 1. Install Selenium
In your Jupyter notebook or terminal:

```bash
pip install selenium

### 2. Download ChromeDriver
Get the correct version for your Chrome browser:
https://chromedriver.chromium.org/downloads

Place chromedriver.exe in your project folder or add it to system PATH.

### 3. Run the Notebook
Open 01_login_test.ipynb in Jupyter

Execute each cell to run the test

📂 Project Structure

ui-tests-saucedemo/
├── 01_login_test.ipynb      # Jupyter notebook with Selenium test
├── requirements.txt         # Dependencies
├── chromedriver.exe         # Chrome driver (optional if in PATH)
└── README.md                # Project description

🧪 Sample Code (Jupyter)

# driver.get("https://www.saucedemo.com/")
# driver.find_element(By.ID, "user-name").send_keys("standard_user")
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# driver.find_element(By.ID, "login-button").click()
# assert "inventory" in driver.current_url

💡 Notes
This is a learning project as part of a QA automation portfolio

The site is intended for testing and demo purposes only

🛠 Created as part of a personal QA portfolio.
📬 Feel free to open issues or suggestions!