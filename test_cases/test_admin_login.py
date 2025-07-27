import pytest
from selenium.webdriver.common.by import By
from base_pages.login_admin_page import LoginAdminPage
from test_cases.conftest import setup
from utilities.custom_logger import LogMaker
from utilities.read_properties import ReadConfig as RC


class TestAdminLogin:

    admin_page_url = RC.get_admin_page_url()
    username = RC.get_username()
    password = RC.get_password()
    invalid_username = RC.get_invalid_username()
    logger = LogMaker.create_log()

    @pytest.mark.regression
    def test_title_verification(self, setup):
        self.logger.info("***************Test Admin Login****************")
        self.logger.info("***************Admin Page Title Verification****************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        actual_title = self.driver.title
        expected_title = "nopCommerce demo store. Login"

        if actual_title == expected_title:
            self.logger.info("***************test_title_verification title matched****************")

            assert True
            self.driver.close()
        else:
            self.logger.info("***************test_title_verification title unmatched****************")

            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_login(self, setup):
        self.logger.info("***************Valid Admin Login****************")

        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_login_page = LoginAdminPage(self.driver)
        self.admin_login_page.enter_username(self.username)
        self.admin_login_page.enter_password(self.password)
        self.admin_login_page.click_login_btn()

        actual_dashboard_text = self.driver.find_element(By.CSS_SELECTOR, "div[class='content-header'] h1").text

        if actual_dashboard_text == "Dashboard":
            self.logger.info("***************test_valid_login successful***************")

            assert True
            self.admin_login_page.click_logout_btn()
            self.driver.close()
        else:
            self.logger.info("***************test_valid_login unsuccessful***************")
            self.admin_login_page.click_logout_btn()
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalid_login(self, setup):
        self.logger.info("***************Invalid Admin Login****************")

        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_login_page = LoginAdminPage(self.driver)
        self.admin_login_page.enter_username(self.invalid_username)
        self.admin_login_page.enter_password(self.password)
        self.admin_login_page.click_login_btn()

        error_message = self.driver.find_element(By.CSS_SELECTOR, "div[class='message-error validation-summary-errors'] ul li").text

        if error_message == "No customer account found":
            self.logger.info("***************test_invalid_login successful***************")

            assert True
            self.driver.close()
        else:
            self.logger.info("***************test_invalid_login successful***************")

            self.driver.close()
            assert False
