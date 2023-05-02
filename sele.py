from selenium import webdriver
from bs4 import BeautifulSoup
import time

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword
print(url)

driver = webdriver.Chrome()

driver.get(url)
time.sleep(3)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

items = soup.select('.api_ani_send')

rank_num = 1

for area in items:
    ad = area.select_one(".link_ad")
    if ad:
        continue 

    print(f"<<<{rank_num}>>>")

    title = area.select_one('.api_txt_lines.total_tit')
    name = area.select_one('.sub_txt.sub_name')
    print(name.text)
    print(title.text)
    print(title['href'])
    print()

    rank_num += 1
