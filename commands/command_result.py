import discord
from discord.ext import commands
from KBO_crawler import get_kbo_result

# =================================================================================================================

# 경기 결과 임베드 생성 함수
def make_result_embed():
    data = get_kbo_result()
    results = data["results"]
    current_date = data["date"]

    embed = discord.Embed(
        title = "⚾ 오늘의 KBO 경기 결과",
        color = 0xE53935,
        description = f"📅 **{current_date}** 경기 결과"
    )

    # 결과 텍스트 생성
    if results and "notice" in results[0]:
        result_text = results[0]["notice"]

    else:
        result_text = ""

        for game in results:
            time = game.get("time", "")
            team1 = game.get("team1", "")
            team2 = game.get("team2", "")
            stadium = game.get("stadium", "")
            score = game.get("score", "")
            inning = game.get("inning", "")
            pitcher = game.get("pitcher", "")
            hitter = game.get("hitter", "")
            emoji1 = game.get("emoji1", "⚾")
            emoji2 = game.get("emoji2", "⚾")

            result_text += f"@ {stadium} {time} | {emoji1} {team1} {score} {team2} {emoji2} | {inning} | 투수: {pitcher} | 타자: {hitter}\n"

    # 임베드 필드 추가
    now = discord.utils.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    embed.add_field(name = "📊 경기 결과", value = result_text, inline = False)
    embed.set_footer(text = f"📊 KBO 공식 홈페이지 | 생성: {now}")

    return embed

# =================================================================================================================

# 명령어 설정 함수
async def setup(bot : commands.Bot):
    @bot.tree.command(name = "결과", description = "오늘의 KBO 경기 결과를 확인합니다")

    async def _result_command(interaction : discord.Interaction):
        await interaction.response.defer()
        embed = make_result_embed()
        await interaction.followup.send(embed = embed)

    print("04. KBO 결과 명령어 로드 완료")