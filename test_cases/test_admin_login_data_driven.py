import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.login_admin_page import LoginAdminPage
from test_cases.conftest import setup
from utilities import excel_utils
from utilities.custom_logger import LogMaker
from utilities.read_properties import ReadConfig as RC


class TestAdminLoginDataDriven:

    admin_page_url = RC.get_admin_page_url()
    logger = LogMaker.create_log()
    test_data_path = ".//test_data//admin_test_data.xlsx"
    status_list = []

    def test_valid_login_data_driven(self, setup):
        self.logger.info("***************Valid Admin Login With Data Driven****************")

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_login_page = LoginAdminPage(self.driver)

        self.rows = excel_utils.get_row_count(self.test_data_path,"Sheet1")
        print(f"num of rows {self.rows}")

        for r in range(2,self.rows+1):
            self.username = excel_utils.read_data(self.test_data_path,"Sheet1",r,1)
            self.password = excel_utils.read_data(self.test_data_path,"Sheet1",r,2)
            self.exp_login = excel_utils.read_data(self.test_data_path,"Sheet1",r,3)

            self.admin_login_page.enter_username(self.username)
            self.admin_login_page.enter_password(self.password)
            self.admin_login_page.click_login_btn()
            time.sleep(5)
            actual_dashboard_text = self.driver.title
            exp_dashboard_text = "Dashboard / nopCommerce administration"

            if actual_dashboard_text == exp_dashboard_text:
                print(self.exp_login)
                if self.exp_login == "yes":
                    self.logger.info("***************data driven test_valid_login successful***************")
                    self.status_list.append("Pass")
                    self.admin_login_page.click_logout_btn()
                elif self.exp_login == "no":
                    self.logger.info("***************data driven test_valid_login unsuccessful***************")
                    self.status_list.append("Fail")
                    self.admin_login_page.click_logout_btn()
            elif actual_dashboard_text != exp_dashboard_text:
                if self.exp_login == "yes":
                    self.logger.info("***************data driven test_valid_login unsuccessful***************")
                    self.status_list.append("Fail")
                elif self.exp_login == "no":
                    self.logger.info("***************data driven test_valid_login successful***************")
                    self.status_list.append("Pass")
            time.sleep(5)

        print(f"Status List is {self.status_list}")
        self.driver.close()
        if "Fail" in self.status_list:
            self.logger.info("Admin Login Data Driven Test is Failed")
            assert False
        else:
            self.logger.info("Admin Login Data Driven Test is Passed")
            assert True
