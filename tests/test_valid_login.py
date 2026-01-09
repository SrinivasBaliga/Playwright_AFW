from generics.base_test import BaseTest
from page.login_page import LoginPage
from page.home_page import HomePage
from generics.utility import Utility

class Test_ValidLogin(BaseTest):

    def test_valid_login(self):

        print("reading test data from excel")
        un=Utility.read_xl( self.data_path+"/input.xlsx","ValidLogin",2,1)
        pw=Utility.read_xl( self.data_path+"/input.xlsx","ValidLogin",2,2)

        print("enter valid username")
        login_page=LoginPage(self.page)
        login_page.set_username(un)

        print("enter valid password")
        login_page.set_password(pw)

        print("click on go button")
        login_page.click_go_button()

        print(" verify that home page is displayed...")
        home_page=HomePage(self.page)
        result=home_page.verify_home_page_is_displayed()
        assert result