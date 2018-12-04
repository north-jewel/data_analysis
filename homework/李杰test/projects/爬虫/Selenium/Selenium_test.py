from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://www.douyu.com/g_CF')# 打开浏览器并输入网址
content_list = driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')#element加s 获取的是列表
for i in content_list:
    author = i.find_element_by_xpath('.//span[@class="dy-name ellipsis fl"]').text# 加 . 代表获取所有符合的
    numb = i.find_element_by_xpath('.//span[@class="dy-num fr"]').text
    print(author,numb)
time.sleep(1)#防止浏览器来不及反应
driver.find_element_by_xpath('.//*[@id="J-pager"]/a[4]').click()#翻下一页
print(content_list)
time.sleep(2)

driver.quit()     #自动关闭浏览器