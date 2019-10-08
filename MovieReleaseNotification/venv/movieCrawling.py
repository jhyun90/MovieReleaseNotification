import requests
from bs4 import BeautifulSoup

# 텔레그램 봇
import telegram
# import telepot

from apscheduler.schedulers.blocking import BlockingScheduler

url = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20191010'


def job_function():
    html = requests.get(url)
    # print(html.text)

    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong'))

    # 영화 제목 출력
    # title_list = soup.select('div.info-movie')
    # print(title_list)
    #
    # for i in title_list:
    #     title = i.select_one('a > strong').text.strip()
    #     print(title)
    # print()

    # 영화 티켓 오픈 알림을 위한 텔레그램 봇 객체 생성
    # bot = telepot.Bot(token='963319881:AAE-EQDUlm5QrxuLYCqE0TbfBKem0xsZ73E')
    bot = telegram.Bot(token='963319881:AAE-EQDUlm5QrxuLYCqE0TbfBKem0xsZ73E')

    # IMAX 상영 여부 출력
    # imax = soup.select_one('span.imax')
    # print(imax, '\n')
    imax_list = soup.select('span.imax')
    # print(imax_list, '\n')

    print("IMAX 상영관 영화 목록")
    print("-----------------")
    for imax in imax_list:
        # IMAX 상영관 예매 가능 영화의 전체 상영 시간표 조회
        imax_movie = imax.find_parent('div', class_='col-times')
        # print(imax_movie)

        # IMAX 상영관 영화 제목 조회
        imax_movie_title = imax_movie.select_one('div.info-movie > a > strong').text.strip()
        # print(imax_movie_title)

        # 텔레그램 봇을 통한 IMAX 상영관 티켓 오픈 알림
        print(imax_movie_title + " IMAX 티켓 오픈! 예매가 시작되었습니다!")
        bot.sendMessage(chat_id='954588678', text=imax_movie_title + " IMAX 티켓 오픈! 예매가 시작되었습니다!")

        # 티켓 오픈 알림 이후에는 동작 중지
        schedule.pause()


# APScheduler
schedule = BlockingScheduler()
schedule.add_job(job_function, 'interval', seconds=10)
schedule.start()
