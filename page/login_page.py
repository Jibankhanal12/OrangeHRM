import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.forgot_password_link = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
        self.reset_password_button = (By.XPATH, "//button[@type='submit']")
        self.invalid_credential = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
        self.email_input_field = (By.NAME, "username")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def enter_email(self, email_address):
        self.driver.find_element(*self.email_input_field).send_keys(email_address)

    def click_forgot_password(self):
        self.driver.find_element(*self.forgot_password_link).click()

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def click_submit(self):
        self.driver.find_element(*self.reset_password_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def forgot_password(self, email_address):
        self.click_forgot_password()
        self.enter_email(email_address)
        self.click_submit()
