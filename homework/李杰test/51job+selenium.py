from selenium import webdriver
import time

def open51job(url,keys):
    drive = webdriver.Chrome()
    drive.get(url)
    elem = drive.find_element_by_id('kwdselectid') #搜索框id
    elem.clear()#清除搜索框数据
    elem.send_keys(keys)#输入数据

    time.sleep(1)
    elem.find_element_by_xpath('//*[@id="work_position_input"]').click()
    time.sleep(1)
    #elem.find_element_by_xpath('work_position_click_multiple_selected_each_010000').click()#取消城市
    elem.find_element_by_xpath('//*[@id="work_position_click_center_right_list_category_000000_010000"]').click()#点击城市
    time.sleep(1)
    elem.find_element_by_xpath('//*[@id="work_position_click_bottom_save"]').click()#选完城市并确定
    time.sleep(1)
    elem.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/button').click()
    time.sleep(2)
    info = drive.find_elements_by_xpath('//*[@id="resultList"]/div[@class="el"]')
    for i in info:
        autho = i.find_element_by_xpath('.//a[@target="_blank"]')
        href = i.find_element_by_xpath('.//a[@target="_blank"]').get_attribute("href")
        title = i.find_element_by_xpath('.//a[@target="_blank"]').get_attribute('title')
        print(autho.text)
        print(href)
        print(title)
    print(info)
    print(len(info))



if __name__ == '__main__':
    url = 'https://www.51job.com/'
    keys = input('请输入搜索的关键词')
    open51job(url,keys)
