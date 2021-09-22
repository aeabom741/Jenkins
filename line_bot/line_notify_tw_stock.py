from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import requests

driver = webdriver.Chrome()
driver.get("https://www.cnyes.com/")

js = "scrollTo(0,1500);"
driver.execute_script(js)
sleep(3)
WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='jsx-3562970947 trend-chart'][1]/div/div[2]/div[2]")))

#台灣加權指數
title = driver.find_element_by_xpath("//div[@class='jsx-3562970947 trend-chart'][1]/div/div[1]/div[1]/a").text
amount_increase = driver.find_element_by_xpath("//div[@class='jsx-3562970947 trend-chart'][1]/div/div[1]/div[2]").text
amount = driver.find_element_by_xpath("//div[@class='jsx-3562970947 trend-chart'][1]/div/div[2]/div[1]").text
amount_percent = driver.find_element_by_xpath("//div[@class='jsx-3562970947 trend-chart'][1]/div/div[2]/div[2]").text

# #台灣櫃檯指數
title_2 = driver.find_element_by_xpath("//div[@class='jsx-3562970947 trend-chart'][2]/div/div[1]/div[1]/a").text
amount_increase_2 = driver.find_element_by_xpath("//div[@class='jsx-3562970947 trend-chart'][2]/div/div[1]/div[2]").text
amount_2 = driver.find_element_by_xpath("//div[@class='jsx-3562970947 trend-chart'][2]/div/div[2]/div[1]").text
amount_percent_2 = driver.find_element_by_xpath("//div[@class='jsx-3562970947 trend-chart'][2]/div/div[2]/div[2]").text

driver.quit()

meg = "\n股票名稱:"+title+"\n漲跌幅:"+amount_increase+"\n指數:"+amount+"\n漲跌幅(百分比):"+amount_percent+"\n-------------"+"\n股票名稱:"+title_2+"\n漲跌幅:"+amount_increase_2+"\n指數:"+amount_2+"\n漲跌幅(百分比):"+amount_percent_2

def line_notify(token,msg):
    headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

token = '1kGThp9ORACadsruHBQdcJmzuveT88lDxDxePkZ2pNr'
line_notify(token, meg)
