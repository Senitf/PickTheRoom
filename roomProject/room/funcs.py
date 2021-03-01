import selenium
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Chrome, ChromeOptions

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import requests
from bs4 import BeautifulSoup

from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError
from urllib.error import URLError

import sys

def get_html(url, _keyword):
    '''
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)   

    driver = webdriver.Chrome("/Users/seni/Desktop/crowling test/chromedriver", chrome_options=opts)
    '''
    #크롬 옵션 코드, 테스할때 씀
    html = list()
    driver = webdriver.Chrome("room/chromedriver")
    driver.implicitly_wait(10)
    driver.get(url)
    #웹 드라이버 여는 작업

    element = driver.find_element_by_id("hotel_search")
    element.send_keys(_keyword)
    time.sleep(2) 
    element.send_keys(Keys.ARROW_DOWN)
    time.sleep(2) 
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)
    time.sleep(1)
    element = driver.find_element_by_xpath("//a[@class='btn_search_confirm sp_hotel']").click()
    time.sleep(2)
    html.append(driver.page_source)
    time.sleep(2)
    
    while driver.find_elements_by_xpath("//a[@class='direction sp_hotel_bf next']"):
        element = driver.find_element_by_xpath("//a[@class='direction sp_hotel_bf next']").click()
        time.sleep(2)
        html.append(driver.page_source)
        time.sleep(2)

    #다음 페이지로 넘기면서 html 저장
    return html

def parse_html(html):

    room_list = list()

    for html_idx in html:

        soup = BeautifulSoup(html_idx, 'html.parser')
        room_area = soup.find_all("div",{"class": "hotel_info"})

        for room_idx in room_area:
            tmp = room_idx.find("strong", {"class":"hotel_name_ko ng-binding"})
            _title = tmp.text
            tmp = room_idx.find("span", {"class":"star_txt ng-binding"})
            _rating = tmp.text
            tmp = room_idx.find("a", {"class":"instance sp_hotel_bf ng-binding"})
            _distance = tmp.text
            tmp = room_idx.find("em", {"class":"ng-binding"})
            _charge = tmp.text

            pictmp = room_idx.find("div", {"class":"img_wrap"}).next_sibling
            imgUrl = pictmp.find("img")

            if imgUrl != None:
                _img = imgUrl['src']
            else:
                _img = ''
            #이미지 url만 저장

            '''
            if imgUrl != None:
                with urlopen(imgUrl['src']) as f:
                    with open('./room/img/' + _title +'.jpg','wb') as h:
                        img = f.read() #이미지 읽기
                        h.write(img)
            #이미지 폴더에 다운 받을 때
            '''

            room_list.append([_title, _rating, _distance, _charge, _img])

    return room_list
#원하는 정보 뽑아서 찾는 과정

def crawling(_keyword):

    URL = 'https://hotel.naver.com/hotels/main'
    #sys.stdout = open('output.txt','w')
    print(parse_html(get_html(URL, _keyword)))
    #따로 출력을 텍스트파일로 만들고 싶을때 주석 해제

    #return parse_html(get_html(URL, _keyword))
#크롤링하는 메인 함수, 여기서 시작함


def set_weight(_input):
    weight_li = [0, 0, 0, 0, 0]
    dic = {0 :_input[0], 1 :_input[1], 2 :_input[2], 3 :_input[3], 4 :_input[4]}
    dic.sort()
    weight = 0.1
    for idx in dic.keys:
        weight_li[idx] = weight
        weight = weight + 0.2
    return weight_li
#기준 별 가중치 설정

'''
hotel A
0.2 km 4 
150000 2 -> 0 - 1 weight // reverse sort() -> 0.1 0.3 0.5 0.7 0.9
평점(8) 4 
if dataA = ""  
'''

def calc(_weight, _input):
    _sum = 0
    for i in _input:
        _sum = _sum + i
    calc_val = 0
    for i in range(5):
        calc_val = calc_val + _weight[i] * (_input[i] / _sum)
    return calc_val
#SAW 알고리즘 적용한 결과 계산
'''
user A
1
2
5 * hotel A weight -> calculated value = hotel A 에 대한 user A 의 선호도 -> 선호도 가장 높은거
3
2
'''

print(crawling('4호선 범계역'))