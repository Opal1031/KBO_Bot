import requests
import time

from bs4 import BeautifulSoup
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# =================================================================================================================

KBO_BASE_URL = "https://www.koreabaseball.com/"
TEAM_EMOJIS = {
    "LG" : "🧑‍🤝‍🧑", "KIA" : "🐯", "삼성" : "🦁", "KT" : "🧙‍♂️", "SSG" : "🛸",
    "롯데" : "🕊️", "한화" : "🦅", "NC" : "🦖", "두산" : "🐻", "키움" : "🦸"
}

# =================================================================================================================

# 일정 크롤링
def get_dynamic_schedule():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options = chrome_options)
    driver.get("https://www.koreabaseball.com/")
    time.sleep(2)
    html = driver.page_source
    driver.quit()

    # 요청 보내기
    soup = BeautifulSoup(html, "html.parser")

    # 일정 데이터 추출
    schedule_section = soup.find("div", class_ = "today-game")
    schedule = []

    if schedule_section:
        game_list = schedule_section.find("ul", class_ = "game-list-n")
        if game_list:
            for game_li in game_list.find_all("li", class_ = "game-cont"):
                top_ul = game_li.find("div", class_ = "top").find("ul")
                stadium = top_ul.find_all("li")[0].get_text(strip = True)
                time_ = top_ul.find_all("li")[2].get_text(strip = True)
                info_div = game_li.find("div", class_ = "info")
                away_team = info_div.find("div", class_ = "team away").find("img")["alt"]
                home_team = info_div.find("div", class_ = "team home").find("img")["alt"]
                schedule.append({
                    "time" : time_,
                    "team1" : away_team,
                    "team2" : home_team,
                    "stadium" : stadium
                })

    # 예외 처리
    if not schedule:
        schedule = [
            {"time": "", "team1": "", "team2": "", "stadium": "", "notice": "오늘 예정된 경기가 없거나 취소되었습니다."}
        ]

    # 데이터 반환
    return {
        "schedule": schedule,
        "date": datetime.now().strftime("%Y년 %m월 %d일")
    }

# =================================================================================================================

# 순위 크롤링
def get_kbo_data():
    ranking_url = KBO_BASE_URL + "Record/TeamRank/TeamRankDaily.aspx"
    headers = {"User-Agent": "Mozilla/5.0"}

    # 요청 보내기
    response = requests.get(ranking_url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    # 순위 테이블 찾기
    ranking_table = soup.find("table", class_ = "tData")
    tbody = ranking_table.find("tbody")
    rows = tbody.find_all("tr")

    # 순위 데이터 추출
    rankings = []
    for row in rows[:10]:
        cols = row.find_all('td')
        if (len(cols) >= 7):
            rank = cols[0].get_text(strip = True)
            team = cols[1].get_text(strip = True)
            wins = cols[3].get_text(strip = True)
            losses = cols[4].get_text(strip = True)
            draws = cols[5].get_text(strip = True)
            win_rate = cols[6].get_text(strip = True)
            rankings.append({
                "rank" : rank,
                "team" : team,
                "wins" : wins,
                "losses" : losses,
                "draws" : draws,
                "win_rate" : win_rate,
                "emoji" : TEAM_EMOJIS.get(team, "⚾")
            })

    # 데이터 반환
    return {
        "rankings" : rankings,
        "team_emojis" : TEAM_EMOJIS,
        "date" : datetime.now().strftime("%Y년 %m월 %d일")
    }