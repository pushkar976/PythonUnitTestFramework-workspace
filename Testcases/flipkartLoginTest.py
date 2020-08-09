import sys
sys.path.append("E:\\Python\\UnitTest_Framework")

from selenium import webdriver
from pageObjects.flipkartLogin import flipkartLogin
import HtmlTestRunner
import unittest
import time

class loginTest(unittest.TestCase):
    url = "https://www.flipkart.com"
    myDataFile = open("C:/Users/admin/Desktop/loginData.txt", "r")
    contents = myDataFile.readline().split()
    print(contents)

    userID = contents[0]
    pass_word = contents[1]

    FFdriverloc = 'E:\\Python\\lib\\geckodriver'
    driver = webdriver.Firefox(executable_path=FFdriverloc)

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)

    def test_login(self):
        flipLogin = flipkartLogin(self.driver)
        flipLogin.setUserName(self.userID)
        flipLogin.setPassword(self.pass_word)
        flipLogin.clickLoginButton()
        time.sleep(3)
        print('Title of the page : ',self.driver.title)
        self.assertEqual("Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!",
                         self.driver.title,'Webpage title is matching')
        time.sleep(3)

    @classmethod
    def tearDownClass(cls) :
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:\\Python\\UnitTest_Framework\\Reports'))


