import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utillties.read_property import Read_Config
from utillties.custom_logger import  log_Maker
class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_url()
    username = Read_Config.get_admin_username()
    invalid_username = Read_Config.get_invalid_user()
    password = Read_Config.get_admin_password()
    logger = log_Maker.log_gen()
    def test_title_verification(self, setup):
        self.logger.info("*****************Test_01_Admin_Login****************")
        self.logger.info("*****************verification of admin login page title***********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            self.logger.info("*****************test_title_verification title matched**************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("*************test_title_verification title not matched*************")
            self.driver.close()
            assert False
    def test_valid_admin_login(self, setup):
        self.logger.info("****************test_valid_admin_login started**************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver) #create an objects from page class and give it access to browser
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']//h1").text
        if act_dashboard_text == "Dashboard":
            self.logger.info("*************Dashboard text found*************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False
    def test_invalid_admin_login(self, setup):
        self.logger.info("*************test_invalid_admin_login started**************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver) #create an objects from page class and give it access to browser
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH, "//li").text
        if error_message == "No customer account found":
            self.logger.info("***************test_invalid_admin_login error message is matched**************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False
    # def test_logout(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.admin_page_url)
    #     self.admin_lp = Login_Admin_Page(self.driver)
    #     self.admin_lp.enter_username(self.username)
    #     self.admin_lp.enter_password(self.password)
    #     self.admin_lp.click_login()
    #     self.admin_lp.click_logout()
    #     act_logout = self.driver.find_element(By.XPATH, "//button[@type='submit']").text
    #     if act_logout == "LOG IN":
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot(".\\screenshots\\test_logout.png")
    #         self.driver.close()
    #         assert False




