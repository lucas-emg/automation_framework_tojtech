from base_test import BaseTest
import time

class TestNewTest(BaseTest):

    def test_page_loads(self):
        time.sleep(10)
        page_title = self.driver.title
        print(page_title)