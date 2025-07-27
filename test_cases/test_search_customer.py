import time

import pytest

from base_pages.add_customer_page import AddCustomerPage
from base_pages.login_admin_page import LoginAdminPage
from base_pages.search_customer_page import SearchCustomerPage
from utilities.custom_logger import LogMaker
from utilities.read_properties import ReadConfig
from test_cases.conftest import setup


class TestSearchCustomer:
    admin_page_url = ReadConfig.get_admin_page_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogMaker.create_log()
    input_email_for_search = "Ttysp@gmail.com"
    input_first_name_for_search = "RAM"
    input_last_name_for_search = "Gannoj"
    input_company_name_for_search = "busyQA"

    def search_customer_setup(self, setup):
        self.logger.info("****************Test Search Customer By Email*************************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_login = LoginAdminPage(self.driver)
        self.admin_login.enter_username(self.username)
        self.admin_login.enter_password(self.password)
        self.admin_login.click_login_btn()
        self.logger.info("********************Login Successful*************************")
        self.logger.info("********************Navigating to Customer Page*************************")
        self.add_customer = AddCustomerPage(self.driver)
        self.add_customer.click_customer()
        self.add_customer.click_customer_in_menu()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.search_customer_setup(setup)
        self.logger.info("********************Start Testing Search Customer By Email*************************")
        self.search_customer = SearchCustomerPage(self.driver)
        self.search_customer.enter_email(self.input_email_for_search)
        self.search_customer.click_search_btn()
        time.sleep(3)
        is_email_present = self.search_customer.search_customer_by_email(self.input_email_for_search)
        if is_email_present == True:
            assert True
            self.logger.info("********************Test Search Customer By Email Passed*************************")
            self.driver.close()
        else:
            self.logger.info("********************Test Search Customer By Email Failed*************************")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):
        self.search_customer_setup(setup)
        self.logger.info("********************Start Testing Search Customer By Name*************************")
        self.search_customer = SearchCustomerPage(self.driver)
        self.search_customer.enter_first_name(self.input_first_name_for_search)
        self.search_customer.enter_last_name(self.input_last_name_for_search)
        self.search_customer.click_search_btn()
        name = self.input_first_name_for_search +" "+ self.input_last_name_for_search
        time.sleep(3)
        is_name_present = self.search_customer.search_customer_by_name(name)
        if is_name_present == True:
            assert True
            self.logger.info("********************Test Search Customer By Name Passed*************************")
            self.driver.close()
        else:
            self.logger.info("********************Test Search Customer By Name Failed*************************")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_company(self, setup):
        self.search_customer_setup(setup)
        self.logger.info("********************Start Testing Search Customer By Company*************************")
        self.search_customer = SearchCustomerPage(self.driver)
        self.search_customer.enter_company_name(self.input_company_name_for_search)
        self.search_customer.click_search_btn()
        time.sleep(3)
        is_company_present = self.search_customer.search_customer_by_company(self.input_company_name_for_search)
        if is_company_present == True:
            assert True
            self.logger.info("********************Test Search Customer By Company Passed*************************")
            self.driver.close()
        else:
            self.logger.info("********************Test Search Customer By Company Failed*************************")
            self.driver.close()
            assert False



