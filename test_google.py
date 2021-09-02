import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time,re

class test_google(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.google.com")
    
    def tearDown(self):
        self.driver.quit()
    
    #webpage testcase
    def test_url(self):
        self.url =  self.driver.current_url
        self.assertEqual(self.url,"https://www.google.com/?gws_rd=ssl")

    def test_title(self):
        self.title = self.driver.title
        self.assertEqual(self.title,"Google")

    #Header testcase
    def test_about_google(self):
        self.about_google = WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable((By.LINK_TEXT,"關於 Google")))
        self.about_google.click()
        self.title = self.driver.title
        self.assertEqual(self.title,"Google - 關於",msg="Error")

    def test_google_shop(self):
        self.shop = WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable((By.LINK_TEXT,"Google 商店")))
        self.shop.click()
        self.title = self.driver.title
        self.assertIn("Google 商店",self.title,msg="error")

    def test_mail(self):
        self.mail = WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable((By.LINK_TEXT,"Gmail")))
        self.mail.click()
        self.title = self.driver.title
        self.assertIn("Gmail",self.title,msg="Error")

    def test_picture(self):
        self.picture = WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable((By.LINK_TEXT,"圖片")))
        self.picture.click()
        self.title = self.driver.title
        self.assertEqual(self.title,'Google 圖片')

    def test_app_menu(self):
        self.menu = WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='gb_C']")))
        self.menu.click()
        self.driver.switch_to_frame(0)
        self.menu_window = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@id='yDmH0d']")))
        self.assertTrue(self.menu_window.is_displayed())

    #search filed testcase
    def test_search_filed(self):
        self.search_file = WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='q']")))
        self.assertTrue(self.search_file,"can't find filed")

    def test_search_type(self):
        self.search_type = WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='q']")))
        self.search_type.send_keys("name")
        self.assertIn("name",self.search_type.get_attribute("value"),msg="error")

    def test_search_button_exsit(self):
        self.search_button = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//input[@name='btnK']")))
        self.assertIn("Google 搜尋",self.search_button.get_attribute("value"),msg="error")
    
    def test_good_luck_exist(self):
        self.good_luck_button = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//input[@class='RNmpXc']")))
        self.assertEqual("好手氣",self.good_luck_button.get_attribute("value"),msg='error')

    def test_search_function(self):
        self.search = WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='q']")))
        self.button = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//input[@name='btnK']")))
        self.search.send_keys("selenium")
        self.search.click()
        self.button.click()

    def test_search_result(self):
        self.search = WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='q']")))
        self.button = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//input[@name='btnK']")))        
        self.search.send_keys("selenium")
        self.search.click()
        self.button.click()
        time.sleep(3)
        self.title = self.driver.title
        self.assertEqual(self.title,"selenium - Google 搜尋")

    #test footercase
    def test_footer_commercial(self):
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='KxwPGc AghGtd']")))
        self.footer_commercial = self.driver.find_elements_by_xpath("//a[@class='pHiOh']")
        self.footer_commercial[0].click()
        self.title = self.driver.title
        self.assertIn("Google Ads",self.title,msg='Error')

    def test_footer_shop(self):
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='KxwPGc AghGtd']")))
        self.footer_shop = self.driver.find_elements_by_xpath("//a[@class='pHiOh']")
        self.footer_shop[1].click()
        self.title = self.driver.title
        self.assertIn("Google 我的商家",self.title,msg="Error")

    def test_footer_search_function(self):
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='KxwPGc AghGtd']")))
        self.footer_search_function = self.driver.find_elements_by_xpath("//a[@class='pHiOh']")
        self.footer_search_function[2].click()
        self.title = self.driver.title
        self.assertIn("Google 搜尋的運作方式",self.title,msg="Error")

    def test_footer_privacy(self):
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='KxwPGc iTjxkf']")))
        self.footer_privacy = self.driver.find_elements_by_xpath("//div[@class='KxwPGc iTjxkf']/a[@class='pHiOh']")
        self.footer_privacy[0].click()
        self.title = self.driver.title
        self.assertIn("隱私權政策",self.title,msg = "Error")
    
    def test_footer_service(self):
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='KxwPGc iTjxkf']")))
        self.footer_service = self.driver.find_elements_by_xpath("//div[@class='KxwPGc iTjxkf']/a[@class='pHiOh']")
        self.footer_service[1].click()
        self.title = self.driver.title
        self.assertIn("Google 服務條款",self.title,msg="Error")
    
    #Setting testcase
    def test__search_setting(self):
        self.setting =  WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//button[@class='EzVRq']")))
        self.setting.click()
        self.search_setting  = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"搜尋設定")))
        self.search_setting.click()         
        self.assertEqual(self.driver.title,"搜尋設定",msg="Error")

    def test_higher_search_setting(self):
        self.setting = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//button[@class='EzVRq']")))
        self.setting.click()
        self.higer_search_setting = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"進階搜尋")))
        self.higer_search_setting.click()
        self.assertEqual(self.driver.title,"Google 進階搜尋",msg="Error")

    def test_search_history(self):
        self.setting = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//button[@class='EzVRq']")))
        self.setting.click()
        self.search_history = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"你在 Google 搜尋中的資料")))
        self.search_history.click()
        self.assertEqual(self.driver.title,"您在 Google 搜尋中的資料")

    def test_history(self):
        self.setting = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//button[@class='EzVRq']")))
        self.setting.click()
        self.search_history = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"搜尋記錄")))
        self.search_history.click()
        self.assertEqual(self.driver.title,"Google - 個人化搜尋結果")

    def test_search_describe(self):
        self.setting = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//button[@class='EzVRq']")))
        self.setting.click()
        self.search_describe = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"搜尋說明")))
        self.search_describe.click()
        self.assertEqual(self.driver.title,"Google 搜尋說明",msg="error")

    # def test_advice(self):
    #     self.setting = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//button[@class='EzVRq']")))
    #     self.setting.click()
    #     self.search_advice = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"提供意見")))
    #     self.search_advice.click()
    #     self.search_advice_title = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//h1[@id='google-feedback-wizard-h1']")))
    #     self.assertEqual(self.driver.title,"提供意見",msg="error")


if __name__ == "__main__":
    unittest.main()




