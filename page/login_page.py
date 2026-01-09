from playwright.sync_api._generated import Page #we have imported to get auto suggestion

class LoginPage:

    __username:str
    __password:str
    __go_button:str

    def __init__(self,page:Page):
        self.page=page
        self.__username="#input-username"
        self.__password="#input-password"
        self.__go_button="//*[text()='Go']"

    def set_username(self,un):
        self.page.locator(self.__username).fill(un)

    def set_password(self,pw):
        self.page.locator(self.__password).fill(pw)

    def click_go_button(self):
        self.page.locator(self.__go_button).click()