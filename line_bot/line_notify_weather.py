import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6300100")
js = "scrollTo(0,800);"

alert = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//a[@id="marquee_1"]')))
alert.click()
contain = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@id='marquee_2']"))).text

dismiss = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
dismiss.click()

driver.execute_script(js)
Temp = driver.find_element_by_xpath("//span[@class='GT_T']/span[@class='tem-C is-active']").text
body_Temp = driver.find_element_by_xpath("//span[@class='GT_AT']/span[@class='tem-C is-active']").text
driver.quit()

if int(Temp) > 35:
    print("")


msg = "\n"+contain+"\n氣溫:"+Temp+"\n體感溫度:"+body_Temp

#Line BOT
def line_notify(token,msg):
    headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code


token = '1kGThp9ORACadsruHBQdcJmzuveT88lDxDxePkZ2pNr'
line_notify(token, msg)

