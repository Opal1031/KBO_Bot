import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 크롤링 함수
def get_kbo_ranking():
    try:
        # KBO 공식 팀 순위 페이지
        url = "https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        # 요청 보내기
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # 순위 테이블 찾기
        ranking_table = soup.find("table", class_ = "tData")
        tbody = ranking_table.find("tbody")
        rows = tbody.find_all("tr")

        # 현재 날짜
        current_date = datetime.now().strftime("%Y년 %m월 %d일")

        # 메인 임베드
        embed = discord.Embed(
            title = "🏆 KBO 리그 순위",
            color = 0x1E88E5,
            description = f"📅 **{current_date}** 기준",
            timestamp = datetime.now()
        )

        # 팀 이모지 매핑
        team_emojis = {
            'LG': '🐯', 'KIA': '🐅', '삼성': '🦁', 'KT': '🏔️', 'SSG': '🔥',
            '롯데': '🦅', '한화': '🦉', 'NC': '🐨', '두산': '🐻', '키움': '🦸'
        }

        ranking_text = ""

        for row in rows[:10]:
            cols = row.find_all('td')

            if len(cols) >= 7:
                try:
                    rank = int(cols[0].get_text(strip=True))
                    team = cols[1].get_text(strip=True)
                    wins = cols[3].get_text(strip=True)
                    losses = cols[4].get_text(strip=True)
                    draws = cols[5].get_text(strip=True)
                    win_rate = cols[6].get_text(strip=True)

                    # 팀 이모지
                    team_emoji = team_emojis.get(team, '⚾')

                    # 순위별 메달 이모지
                    if rank == 1:
                        rank_emoji = "🥇"
                    elif rank == 2:
                        rank_emoji = "🥈"
                    elif rank == 3:
                        rank_emoji = "🥉"
                    else:
                        rank_emoji = f"`{rank}위`"

                    # 간단한 리스트 형태 (4번 방식)
                    ranking_text += f"{rank_emoji} {team_emoji} **{team}** • {wins}승 {losses}패 {draws}무 • 승률 {win_rate}\n"

                except (IndexError, AttributeError, ValueError):
                    continue

        # 순위 표시
        embed.add_field(name = "📊 팀 순위", value = ranking_text, inline = False)

        # 푸터
        embed.set_footer(text = "📊 KBO 공식 홈페이지")

        return embed

    except requests.RequestException as e:
        return f"KBO 사이트 접속 오류 : {str(e)}"
    except Exception as e:
        return f"순위 정보 처리 중 오류 : {str(e)}"

# 명령어 설정 함수
async def setup(bot: commands.Bot):
    @bot.tree.command(name="순위", description = "KBO 팀 순위를 확인합니다")
    async def _ranking_command(interaction: discord.Interaction):
        await interaction.response.defer()

        ranking_data = get_kbo_ranking()
        await interaction.followup.send(embed=ranking_data)

    print("02. KBO 순위 명령어 로드 완료")