import requests
from bs4 import BeautifulSoup

song_num_text = "javascript:melon.link.goArtistDetail('3055146');"

def get_song_nums(song_num_text):
    song_num = []
    for num in song_num_text:
        if num.isdigit():
            song_num.append(num)

    song_num = "".join(song_num) # 가수의 고유 번호가 리스트로 저장되는데 숫자로 바꿔주기

    return song_num



