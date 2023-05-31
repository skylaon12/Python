# BeautifulSoup에 xml parser 추가하기
# pip install lxml


# 웹 상의 XML 분석하기
import requests
from bs4 import BeautifulSoup


def get_contents(URL):
    source = requests.get(url=URL)
    if source.status_code == 200:
        return source.text


def parse_weather(weather_contents):

    f = open('weather.txt', 'wt', encoding='utf-8')

    soup = BeautifulSoup(weather_contents, 'xml')  # xml 분석기
    # soup.find_all('location')  ['<location>...</location>', '<location>...</location>', ...]

    for location in soup.find_all('location'):

        # location.find('province')        '<province>서울</province>'
        # location.find('province').text   '서울'
        province = location.find('province').text
        city = location.find('city').text

        f.write(f'{province} / {city}\n')  # 서울, 경기도, 인천 / 서울

        # location.find_all('data')  ['<data>...</data>', '<data>...</data>', ...]
        for data in location.find_all('data'):
            tmEf = data.find('tmEf').text
            wf = data.find('wf').text
            tmn = data.find('tmn').text
            tmx = data.find('tmx').text
            rnSt = data.find('rnSt').text
            f.write(f'{tmEf} - {wf}, 최저 {tmn}, 최고 {tmx}, 강수확률 {rnSt}\n')

    f.close()


contents = get_contents('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')  # 실행
parse_weather(contents)
