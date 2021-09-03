from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import unittest

class test_bing(unittest.TestCase):
   
    def setUp(self):     
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.bing.com/")
    
    def tearDown(self):
        self.driver.quit()

    def test_picture(self):
        self.picture = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"圖片")))
        self.picture.click()
        self.assertEqual(self.driver.title,"Bing")
    
    def test_film(self):
        self.film = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"影片")))
        self.film.click()
        self.assertEqual(self.driver.title,"Bing")

    def test_list(self):
        self.list = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//li[@class='scope dots']")))
        self.list.click()
        self.map = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"地圖")))
        self.assertTrue(self.map,msg="error")

    def test_list_map(self):
        self.list = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//li[@class='scope dots']")))
        self.list.click()
        self.map = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"地圖")))
        self.map.click()
        self.assertIn("Bing 地圖",self.driver.title,msg="error")

    def test_list_new(self):
        self.list = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//li[@class='scope dots']")))
        self.list.click()
        self.new = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"新聞")))
        self.new.click()
        self.assertIn("熱門報導",self.driver.title,msg="error")

    def test_list_msn(self):
        self.list = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//li[@class='scope dots']")))
        self.list.click()
        self.msn = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"MSN")))
        self.msn.click()


if __name__ == "__main__":
    unittest.main()