from playwright.sync_api._generated import Page #we have imported to get auto suggestion

class HomePage:

    __logout:str


    def __init__(self,page:Page):
        self.page=page
        self.__logout="//a[text()='Logout']"


    def verify_home_page_is_displayed(self):
        try:
            self.page.locator(self.__logout).wait_for()
            print('Home Page is displayed')
            return True
        except:
            print('Home Page is not displayed')
            return False