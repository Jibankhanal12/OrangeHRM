
import pytest
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from page.login_page import LoginPage


# Fixture to set up and tear down the browser session
@pytest.fixture(scope="function")
def setup_browser():
    # Initializes the Chrome browser, navigates to the OrangeHRM login page, and quits after test execution.

    service1 = Service(executable_path="D:\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service1)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


# Test case for valid login scenario
def test_valid_login(setup_browser):
    # Tests login with valid credentials and verifies that the Dashboard page is displayed.
    driver = setup_browser
    login_page = LoginPage(driver)
    try:
        login_page.login("Admin", "admin123")
        dashboard = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
            (By.XPATH, "//h6[@class ='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")))
        assert "Dashboard" in dashboard.text, "Login failed with valid credentials"
        # Logout after successful login
        driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        sleep(1)
    except(TimeoutException, NoSuchElementException) as e:
        pytest.fail(f"Test Failed:{e}")


# Test case for invalid login scenario
def test_invalid_login(setup_browser):
    # Test login with invalid credentials and verifies that an error message is displayed.
    driver = setup_browser
    login_page = LoginPage(driver)
    try:
        login_page.login("Admin2", "admin1234")
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")))
        assert "Invalid credentials" in error_message.text, "error message is not displayed for invalid credentials"
    except(TimeoutException, NoSuchElementException) as e:
        pytest.fail(f"Test Failed: {e}")


# Test case for login attempt with blank username and password fields
def test_blank_fields(setup_browser):
    # Test login with blank fields and checks for a 'Required' field validation message.
    driver = setup_browser
    login_page = LoginPage(driver)
    try:
        login_page.login("", "")
        error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]")))
        assert "Required" in error_message.text, "error message is not displayed for blank fields"
    except(TimeoutException, NoSuchElementException) as e:
        pytest.fail(f"Test Failed: {e}")


# Test case for forgot password functionality
def test_forgot_password(setup_browser):
    # Test the 'Forgot Password' feature and verifies that a reset link is sent successfully.
    driver = setup_browser
    login_page = LoginPage(driver)
    try:
        login_page.forgot_password("example@gmail.com")
        password_reset_page = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']")))
        assert "Reset Password link sent successfully" in password_reset_page.text, "Failed to sent the password reset link"
    except(TimeoutException, NoSuchElementException) as e:
        pytest.fail(f"Test Failed: {e}")
