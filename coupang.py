import requests
from bs4 import BeautifulSoup

base_url = "https://www.coupang.com/np/search?component=&q="

keyword = input("검색어를 입력해볼까요? : ")

search_url = base_url + keyword

headers = {
    "User-Agent" : "# Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

cookie = {"a": "b"}


req = requests.get(search_url, timeout=5 ,headers=headers, cookies=cookie)

html = req.text

soup = BeautifulSoup(html, "html.parser")

items = soup.select('[class=search-product]')

print(len(items))
