from selenium import webdriver
import time
url = 'http://www.5ifxw.com/vip/'
driver = webdriver.Chrome()
driver.get(url)
valu= driver.find_element_by_class_name('text')
valu.clear()
time.sleep(5)
valu.send_keys('https://v.qq.com/x/cover/gtftsxi3kotnhnh.html')
driver.find_element_by_id('doplayers').click()
time.sleep(2)
a = driver.switch_to.frame('jiekou')
b = driver.find_element_by_xpath('/html/body/div[1]')
print(a)
print(b)
print(valu)
