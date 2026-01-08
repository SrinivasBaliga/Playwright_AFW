import pytest
from playwright.sync_api import sync_playwright
from pyjavaproperties import Properties
import os
class BaseTest:

    @pytest.fixture(autouse=True)
    def pre_condition(self):
        print('\npre condition')

        print("construct the path of config file")
        self.generic_path=os.path.dirname(__file__)
        print("generic_path",self.generic_path)
        config_path=self.generic_path+"/../config.properties"
        print("config_path", config_path)
        self.data_path=self.generic_path+"/../data"
        print('data_path',self.data_path)

        print('Read config file')
        props=Properties()
        props.load(open(config_path))
        ATO=props['ATO']
        NTO=props['NTO']
        APP_URL=props['APP_URL']
        BROWSER=props['BROWSER']
        RUN_LOCAL=props['RUN_LOCAL']
        REMOTE_URL=props['REMOTE_URL']

        print("start playwright software")
        self.playwright = sync_playwright().start()

        if RUN_LOCAL=='yes':
            if BROWSER=='chromium':
                print("open chromium browser in local system")
                self.browser =  self.playwright.chromium.launch(headless=False)

            elif BROWSER=='webkit':
                print("open webkit(safari) browser in local system")
                self.browser = self.playwright.webkit.launch(headless=False)

            else:
                print("open Firefox  browser in local system")
                self.browser = self.playwright.firefox.launch(headless=False)
        else:
            if BROWSER == 'chromium':
                print("open chromium browser in remote system")
                self.browser = self.playwright.chromium.connect(REMOTE_URL)

            elif BROWSER == 'webkit':
                print("open webkit(safari) browser in remote system")
                self.browser =  self.playwright.webkit.connect(REMOTE_URL)

            else:
                print("open Firefox  browser in remote system")
                self.browser =  self.playwright.firefox.connect(REMOTE_URL)

        print("open new page(tab)")
        self.page = self.browser.new_page()

        print("set default timeout to:",ATO,"ms")
        self.page.set_default_timeout(float(ATO))

        print("set default  navigation timeout to:",NTO,"ms")
        self.page.set_default_navigation_timeout(float(NTO))

        print("enter the url:",APP_URL)
        self.page.goto(APP_URL)

    @pytest.fixture(autouse=True)
    def post_condition(self):
        yield
        print('\npost condition')
        print('Close the page')
        self.page.close()

        print("closes the browser")
        self.browser.close()

        print("stop the playwright tool")
        self.playwright.stop()