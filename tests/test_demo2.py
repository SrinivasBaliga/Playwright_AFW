from generics.base_test import BaseTest
from generics.utility import Utility

class TestDemo2(BaseTest):

    def test_demo2(self):
        print('test demo2')
        print("title is:",self.page.title())
        d=Utility.read_xl(self.data_path+"/input.xlsx","demo1",1,1)
        print('data from xl',d)
