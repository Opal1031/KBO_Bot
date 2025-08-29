import discord
from discord.ext import commands
import json
import asyncio
from commands import load_all_commands

# 토큰을 JSON 파일에서 읽어오기
with open("token.json", "r") as f:
    config = json.load(f)
    TOKEN = config["TOKEN"]

# 봇 인스턴스 생성
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)

# 봇 이벤트 핸들러
@bot.event
async def on_ready():
    bar = discord.Game("블루 떼껄룩스 경기력에 감탄하는 중")
    await bot.change_presence(status = discord.Status.online, activity = bar)

    try:
        synced = await bot.tree.sync()
        print(f"슬래시 커맨드 {len(synced)}개 동기화됨")
        print("=====================================")

    except Exception as e:
        print(f"슬래시 커맨드 동기화 실패: {e}")
        print("=====================================")

    print("KBO_Bot RUNNING!!")

# 메인 함수
async def main():
    # 명령어 모듈 로드
    await load_all_commands(bot)

    # 봇 실행
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())