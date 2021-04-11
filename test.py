from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
   #测试前运行的
    def setUp(self):
        self.broswer=webdriver.Firefox()
    #测试后运行的
    def tearDown(self):
        self.broswer.quit()
    #前缀为test的都为测试代码
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.broswer.get('http://localhost:8000')
        self.assertIn('To-Do',self.broswer.title)
        self.fail('Finish the test!')

if __name__=='__main__':
    unittest.main(warnings='ignore')