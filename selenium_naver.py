from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # enter로 검색하기 위해
from webdriver_manager.chrome import ChromeDriverManager 

from bs4 import BeautifulSoup
import time 

options = Options()

options.add_argument("--start-maximized")
options.add_experimental_option('detach', True)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service , options=options)

url = "https://naver.com"

driver.get(url)

time.sleep(2)

driver.find_element(By.ID , "query").send_keys("뉴진스") ## 검색어 '뉴진스' 
time.sleep(2)
 # find_element 단수형, 복수형이 따로 있습니다. 한 개를 찾을지 여러개를 찾을지

driver.find_element(By.CSS_SELECTOR, "#search-btn").click() # 검색버튼 클릭 
time.sleep(2)

#driver.find_elements(By.CLASS_NAME, "menu")[2].click() 
#time.sleep(2)

driver.find_element(By.XPATH, '//*[text()="VIEW"]').click() # VIEW 탭을 찾자
time.sleep(2)

""" driver.find_element(By.NAME, "query").clear()
time.sleep(2)

driver.find_element(By.NAME, "query").send_keys("손흥민")
time.sleep(2)

driver.find_element(By.NAME, "query").send_keys(Keys.ENTER)
time.sleep(2)
"""

for i in range(10):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(1)

html = driver.page_source 

soup = BeautifulSoup(html, "html.parser")

items = soup.select(".api_ani_send")

rank_num = 1
for area in items:
    ad = area.select_one(".link_ad")
    if ad:
        continue
    print(f"<<<{rank_num}>>>")

    title = area.select_one(".api_txt_lines.total_tit")
    name = area.select_one(".sub_txt.sub_name")
    print(name.text)
    print(title.text)
    print(title['href'])
    print()

    rank_num += 1

driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

driver.save_screenshot("11_selenium_naver/naver.jpg")
print("Screen Shot")

driver.quit()
