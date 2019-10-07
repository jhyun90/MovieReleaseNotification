import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20191010'
html = requests.get(url)
# print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
# print(soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong'))

# 영화 제목 출력
title_list = soup.select('div.info-movie')
# print(title_list)

for i in title_list:
    title = i.select_one('a > strong').text.strip()
    print(title)
print()

# IMAX 상영 여부 출력
# print(soup.select_one('span.imax'), '\n')

# imax = soup.select_one('span.imax')
imax_list = soup.select('span.imax')
# print(imax_list, '\n')


print("IMAX 상영관 영화 목록")
print("-----------------")
for imax in imax_list:
    # if imax:
    imax_movie = imax.find_parent('div', class_='col-times')
    # IMAX 상영관 예매 가능 영화의 전체 상영 시간표 조회
    # print(imax_movie)
    # IMAX 상영관 영화 제목 조회
    print(imax_movie.select_one('div.info-movie > a > strong').text.strip())
