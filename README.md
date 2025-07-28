Selenium with Python 

base_pages/
Contains Page Object Model (POM) classes. Each class represents a page in the nopCommerce application and includes functions to interact with the page elements (e.g. login, add customer, search customer).

test_cases/
Holds the actual test scripts. These tests use the page objects from base_pages/ to perform and validate various user workflows.

conftest.py contains Pytest fixtures for browser setup/teardown.

test_data/
Stores test data files like Excel spreadsheets used for data-driven testing (e.g., multiple login credentials).

utilities/
Includes helper functions and utilities such as:

custom_logger.py: for logging test steps and results

read_properties.py: reads configuration from properties file

excel_utils.py: reads test data from Excel files

Note: to run file on different browser:
pytest -s -v .\test_cases\test_admin_login.py --browser firefox
Note: run multiple test parallely
pytest -s -v .\test_cases\test_admin_login.py --browser firefox -n 3
Note: create html reports
pytest -s -v --html reports/report.html .\test_cases\test_admin_login.py
pytest -s -v -m "sanity" --html reports/report.html
