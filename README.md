# OrangeHRM - Automated Testing (Login Page)

This repository contains the automation scripts for testing the **Login Page** of the OrangeHRM website. The tests are implemented using **Selenium** with **Python** and follow the **Page Object Model (POM)** design pattern to ensure better test maintainability and scalability.

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)

## Project Overview

This project aims to automate the login functionality of the OrangeHRM website. The following actions are tested:

- Login with valid credentials.
- Login with invalid credentials (for negative testing).
- Handling error messages for failed login attempts.

The project uses the **Page Object Model (POM)** design pattern, which separates the test scripts from the page-specific actions and elements. This leads to more organized, reusable, and easier-to-maintain code.

## Prerequisites

Before running the automation tests, ensure you have the following installed:

- Python 3.x or higher
- Selenium WebDriver for Python
- WebDriver for the browser you intend to use (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox)
- pytest or unittest (for running the tests)
