import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utillties.read_property import Read_Config
from utillties.custom_logger import  log_Maker
from utillties import excel_utills
class Test_02_Admin_Login_data_driven:
    admin_page_url = Read_Config.get_admin_url()
    logger = log_Maker.log_gen()
    path = ".//test_data//admin_login_data.xlsx"
    status_lists = []
    def test_valid_admin_login_data_driven(self, setup):
        self.logger.info("****************test_valid_admin_login_data_driven started**************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver) #create an objects from page class and give it access to browser
        self.rows = excel_utills.get_row_count(self.path, "Sheet")
        print("num of rows: ", self.rows)

        for r in range(2, self.rows+1):
            self.username = excel_utills.read_data(self.path, "Sheet", r,1)
            self.password = excel_utills.read_data(self.path, "Sheet", r,2)
            self.exp_login = excel_utills.read_data(self.path, "Sheet", r,3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data is passed")
                    self.status_lists.append("pass")
                    self.admin_lp.click_logout()
                elif self.exp_login == "No":
                    self.logger.info("test data is failed")
                    self.status_lists.append("fail")
            elif act_title != exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data is failed")
                    self.status_lists.append("fail")
                    self.admin_lp.click_logout()
                elif self.exp_login == "No":
                    self.logger.info("test data is passed")
                    self.status_lists.append("pass")
        print("status list is: ", self.status_lists)
        if "fail" in self.status_lists:
            self.logger.info("test admin login data failed")
            assert False
        else:
            self.logger.info("test admin login data passed")
            assert True


    

