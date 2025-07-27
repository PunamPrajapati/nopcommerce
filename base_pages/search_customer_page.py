from selenium.webdriver.common.by import By


class SearchCustomerPage:

    text_email_id = "SearchEmail"
    text_first_name_id = "SearchFirstName"
    text_last_name_id = "SearchLastName"
    text_company_name_id = "SearchCompany"
    search_btn = "//button[@id='search-customers']"
    rows_table_xpath = "//table[@class='table table-bordered table-hover table-striped dataTable']/tbody/tr"
    cols_table_xpath = "//table[@class='table table-bordered table-hover table-striped dataTable']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        enter_email = self.driver.find_element(By.ID, self.text_email_id)
        enter_email.clear()
        enter_email.send_keys(email)

    def enter_first_name(self, first_name):
        enter_first_name = self.driver.find_element(By.ID, self.text_first_name_id)
        enter_first_name.clear()
        enter_first_name.send_keys(first_name)

    def enter_last_name(self, last_name):
        enter_last_name = self.driver.find_element(By.ID, self.text_last_name_id)
        enter_last_name.clear()
        enter_last_name.send_keys(last_name)

    def enter_company_name(self, company_name):
        enter_company_name = self.driver.find_element(By.ID, self.text_company_name_id)
        enter_company_name.clear()
        enter_company_name.send_keys(company_name)

    def click_search_btn(self):
        self.driver.find_element(By.XPATH, self.search_btn).click()

    def get_results_table_rows(self):
       return len(self.driver.find_elements(By.XPATH, self.rows_table_xpath))

    def get_results_table_cols(self):
        return len(self.driver.find_elements(By.XPATH, self.cols_table_xpath))

    def search_customer_by_email(self, email):
        email_present_flag = False
        for r in range(1, self.get_results_table_rows()+1):
            customer_email = self.driver.find_element(By.XPATH, "//table[@class='table table-bordered table-hover table-striped dataTable']/tbody/tr["+str(r)+"]/td[2]").text

            if customer_email == email:
                email_present_flag = True
                break
        return email_present_flag

    def search_customer_by_name(self, name):
        name_present_flag = False
        for r in range(1, self.get_results_table_rows()+1):
            customer_name = self.driver.find_element(By.XPATH, "//table[@class='table table-bordered table-hover table-striped dataTable']/tbody/tr["+str(r)+"]/td[3]").text

            if customer_name == name:
                name_present_flag = True
                break
        return name_present_flag

    def search_customer_by_company(self, company_name):
        company_name_present_flag = False
        for r in range(1, self.get_results_table_rows()+1):
            customer_company_name = self.driver.find_element(By.XPATH, "//table[@class='table table-bordered table-hover table-striped dataTable']/tbody/tr["+str(r)+"]/td[5]").text

            if customer_company_name == company_name:
                company_name_present_flag = True
                break
        return company_name_present_flag


