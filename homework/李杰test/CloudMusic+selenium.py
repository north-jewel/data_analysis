from selenium import webdriver
import time

def CloudMusic():
    #url = 'http://music.163.com/song/media/outer/url?id=534544522.mp3'
    url = 'https://music.163.com/artist?id=10559'
    drive = webdriver.Chrome()
    drive.get(url)
    time.sleep(1)
    iframe = drive.switch_to.frame('contentFrame')
    data = drive.find_element_by_id("hotsong-list").find_elements_by_tag_name("tr")
    print(iframe)
    print(data)
    for i in range(len(data)):
        
        content = data[i].find_element_by_class_name("txt")
        href = content.find_element_by_tag_name("a").get_attribute("href")
        title = content.find_element_by_tag_name("b").get_attribute("title")
        print(href,title)
    # for i in iframe:
    #     info = i.find_element_by_xpath('.//*[@id="auto-id-lGTfIeF1G6gHLct1"]/table/tbody')
    #     print(info)

    return url

CloudMusic()
