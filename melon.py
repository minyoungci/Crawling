import requests
from bs4 import BeautifulSoup

def get_song_nums(song_num_text):
    song_num = []
    for num in song_num_text:
        if num.isdigit():
            song_num.append(num)

    song_num = "".join(song_num) # 가수의 고유 번호가 리스트로 저장되는데 숫자로 바꿔주기

    return song_num

# 멜론 차트 100위까지 가수, 노래제목, 앨범 정보 받아오기

headers = {
    "User-Agent" : "# Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

"""lst50 = soup.select(".lst50") # 클래스 앞에는 항상 . 붙여주기

lst100 = soup.select(".lst100")

lst = lst50 + lst100 """ # 멜론 사이트에 50위, 100위 클래스가 나눠져 있어서 더해줌.

# lst = soup.select(".lst50, .lst100") # 위의 코드 세 줄을 한 줄로 바꾸기

lst = soup.find_all(class_=['lst50', 'lst100']) # 위에랑 똑같음

for rank,i in enumerate(lst, 1):
    title = i.select_one(".ellipsis.rank01 a") # ellipsis rank01 클래스를 가져오면 이렇게 되는데 공백은 .으로 항상 해주기 
    # 뒤에 있는 a는 a태그를 정확하게 찾기 -> 출력될 때 공백을 지워줌
    singer = i.select_one(".ellipsis.rank02 > a")
    singer_link = get_song_nums(singer['href'])

    album = i.select_one(".ellipsis.rank03 > a")
    album_link = get_song_nums(album['href'])

    print(f"{rank} : {title.text}")
    print(f"{singer.text} : https://www.melon.com/artist/timeline.htm?artistId={singer_link}")
    print(f"{album.text} : https://www.melon.com/album/detail.htm?albumId={album_link}")
    print() # 가수 : 가수 링크 , 앨범 : 앨범 링크가 나오도록 