import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from base_pages.add_customer_page import AddCustomerPage
from base_pages.login_admin_page import LoginAdminPage
from test_cases.conftest import setup
from utilities.custom_logger import LogMaker
from utilities.read_properties import ReadConfig as RC


def generate_new_email():
    username = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choices(['gmail.com', 'yahoo.com', 'outlook.com', 'example.com'])
    return f'{username}@{domain[0]}'


class TestAddNewCustomer:
    admin_page_url = RC.get_admin_page_url()
    username = RC.get_username()
    password = RC.get_password()
    invalid_username = RC.get_invalid_username()
    logger = LogMaker.create_log()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_new_customer(self, setup):
        self.logger.info("****************Test Add New Customer******************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_login_page  = LoginAdminPage(self.driver)
        self.admin_login_page.enter_username(self.username)
        self.admin_login_page.enter_password(self.password)
        self.admin_login_page.click_login_btn()
        self.logger.info("********************Login Successful************************")
        self.logger.info("********************Start Testing Add New Customer************************")

        self.add_customer = AddCustomerPage(self.driver)
        self.add_customer.click_customer()
        self.add_customer.click_customer_in_menu()
        self.add_customer.click_add_customer()
        self.logger.info("********************Start Form Fillup*****************************")

        email = generate_new_email()
        self.add_customer.enter_email(email)
        self.add_customer.enter_password("123456789")
        self.add_customer.enter_first_name("Punam")
        self.add_customer.enter_last_name("Prajapati")
        self.add_customer.select_gender("Female")
        self.add_customer.enter_company_name("XYZ Company")
        self.add_customer.select_tax_exempt()
        self.add_customer.select_newsletter("nopCommerce admin demo store")
        self.add_customer.select_customer_role("Registered")
        self.add_customer.select_manager_of_vendor("Vendor 1")
        self.add_customer.select_active()
        self.add_customer.select_change_password()
        self.add_customer.enter_admin_comment("This is an automation testing")
        self.add_customer.click_save_btn()
        time.sleep(5)

        customer_add_success_text = "The new customer has been added successfully"
        success_text = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text

        if customer_add_success_text in success_text:
            assert True
            self.logger.info("****************Test Add New Customer Passed*****************")
            self.driver.close()
        else:
            self.logger.info("****************Test Add New Customer Failed*****************")
            self.driver.close()
            assert False


