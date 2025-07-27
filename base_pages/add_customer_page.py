import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomerPage:

    link_customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customers_menuoption_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    link_add_new_customer_xpath = "//a[normalize-space()='Add new']"
    text_email_id = "Email"
    text_password_id = "Password"
    text_first_name_id = "FirstName"
    text_last_name_id = "LastName"
    radio_gender_male_id = "Gender_Male"
    radio_gender_female_id = "Gender_Female"
    text_company_name_id = "Company"
    checkbox_tax_exempt = "IsTaxExempt"
    # Newsletter dropdown clickable element
    test_newsletter_xpath = "//select[@id='SelectedNewsletterSubscriptionStoreIds']/following-sibling::span[contains(@class, 'select2-container')]"
    # Customer roles dropdown clickable element
    test_customer_role_xpath = "//select[@id='SelectedCustomerRoleIds']/following-sibling::span[contains(@class, 'select2-container')]"
    newsletter_option1_xpath = "//option[normalize-space()='nopCommerce admin demo store']"
    customer_role_administrators_xpath = "//li[contains(text(), 'Administrators')]"
    customer_role_guests_xpath = "//li[contains(text(), 'Guests')]"
    customer_role_forum_moderator_xpath = "//li[contains(text(), 'Forum Moderator')]"
    customer_role_registered_xpath = "//li[contains(text(), 'Registered')]"
    customer_role_vendors_xpath = "//li[contains(text(), 'Vendors')]"
    manager_of_vendor_id = "VendorId"
    checkbox_active_id = "Active"
    change_customer_password_id = "MustChangePassword"
    admin_comment_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"
    btn_save_and_edit_xpath = "//button[normalize-space()='Save and Continue Edit']"

    def __init__(self, driver):
        self.driver = driver

    def click_customer(self):
        self.driver.find_element(By.XPATH, self.link_customers_menu_xpath).click()

    def click_customer_in_menu(self):
        customer_in_menu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_customers_menuoption_xpath)))
        customer_in_menu.click()

    def click_add_customer(self):
        self.driver.find_element(By.XPATH, self.link_add_new_customer_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.text_first_name_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.text_last_name_id).send_keys(last_name)

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.radio_gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.radio_gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.radio_gender_female_id).click()

    def enter_company_name(self, company_name):
        self.driver.find_element(By.ID, self.text_company_name_id).send_keys(company_name)

    def select_tax_exempt(self):
        self.driver.find_element(By.ID, self.checkbox_tax_exempt).click()

    def select_active(self):
        self.driver.find_element(By.ID, self.checkbox_active_id).click()

    def select_change_password(self):
        self.driver.find_element(By.ID, self.change_customer_password_id).click()

    def enter_admin_comment(self, admin_comment):
        self.driver.find_element(By.ID, self.admin_comment_id).send_keys(admin_comment)

    def select_newsletter(self, value):
        newsletter_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.test_newsletter_xpath))
        )
        newsletter_dropdown.click()
        time.sleep(3)
        if value == "nopCommerce admin demo store":
            self.driver.find_element(By.XPATH, self.newsletter_option1_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.newsletter_option1_xpath).click()
        newsletter_dropdown.click()

    def select_customer_role(self, value):
        customer_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.test_customer_role_xpath))
        )
        customer_dropdown.click()
        time.sleep(3)

        if value == "Guests":
            self.driver.find_element(By.XPATH, "//li[@title='Registered']//span[@role='presentation'][normalize-space()='×']").click()
            customer_dropdown.click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.customer_role_guests_xpath).click()
        elif value == "Administrators":
            self.driver.find_element(By.XPATH, self.customer_role_administrators_xpath).click()
        elif value == "Vendors":
            self.driver.find_element(By.XPATH, self.customer_role_vendors_xpath).click()
        elif value == "Registered":
            pass
        elif value == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.customer_role_forum_moderator_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.customer_role_administrators_xpath).click()

    def select_manager_of_vendor(self, value):
        drp_down = Select(self.driver.find_element(By.ID, self.manager_of_vendor_id))
        drp_down.select_by_visible_text(value)

    def click_save_btn(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()