from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option = Options()

option.add_experimental_option("detach", True) # 브라우저 화면 꺼짐 막는 옵션

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=option)

url = "https://naver.com"

driver.get(url)

