import discord
from discord.ext import commands
from datetime import datetime
from KBO_crawler import get_dynamic_schedule

# =================================================================================================================

# 일정 임베드 생성 함수
def make_schedule_embed():
    data = get_dynamic_schedule()
    schedule = data["schedule"]
    current_date = data["date"]
    from KBO_crawler import TEAM_EMOJIS

    embed = discord.Embed(
        title = "⚾ 오늘의 KBO 경기 일정",
        color = 0x43A047,
        description = f"📅 **{current_date}** 경기"
    )

    # 일정 텍스트 생성
    if schedule and "notice" in schedule[0]:
        schedule_text = schedule[0]["notice"]

    else:
        schedule_text = ""
        for game in schedule:
            time = game.get("time", "")
            team1 = game.get("team1", "")
            team2 = game.get("team2", "")
            stadium = game.get("stadium", "")
            emoji1 = TEAM_EMOJIS.get(team1, "⚾")
            emoji2 = TEAM_EMOJIS.get(team2, "⚾")
            schedule_text += f"@ {stadium} {time} | {emoji1} {team1} vs {team2} {emoji2}\n"

    # 임베드 필드 추가
    now = discord.utils.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    embed.add_field(name = "경기 일정", value = schedule_text, inline = False)
    embed.set_footer(text = f"KBO 공식 홈페이지 | 생성: {now}")

    return embed

# =================================================================================================================

# 명령어 설정 함수
async def setup(bot : commands.Bot):
    @bot.tree.command(name = "일정", description = "오늘의 KBO 경기 일정을 확인합니다")

    async def _schedule_command(interaction : discord.Interaction):
        await interaction.response.defer()
        embed = make_schedule_embed()
        await interaction.followup.send(embed = embed)

    print("03. KBO 일정 명령어 로드 완료")