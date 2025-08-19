import discord
from discord.ext import commands
from KBO_crawler import get_kbo_data

# =================================================================================================================

# 순위 임베드 생성 함수
def make_ranking_embed():
    data = get_kbo_data()
    rankings = data["rankings"]
    current_date = data["date"]

    embed = discord.Embed(
        title = "🏆 KBO 리그 순위",
        color = 0x1E88E5,
        description = f"📅 **{current_date}** 기준"
    )

    # 순위 텍스트 생성
    ranking_text = ""

    for item in rankings:
        rank = int(item["rank"])
        team = item["team"]
        wins = item["wins"]
        losses = item["losses"]
        draws = item["draws"]
        win_rate = item["win_rate"]
        emoji = item["emoji"]

        if (rank == 1):
            rank_emoji = "🥇"
        elif (rank == 2):
            rank_emoji = "🥈"
        elif (rank == 3):
            rank_emoji = "🥉"
        else:
            rank_emoji = f"`{rank}위`"

        ranking_text += f"{rank_emoji} {emoji} **{team}** • {wins}승 {losses}패 {draws}무 • 승률 {win_rate}\n"

    # 임베드 필드 추가
    now = discord.utils.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    embed.add_field(name = "📊 팀 순위", value = ranking_text, inline = False)
    embed.set_footer(text = f"📊 KBO 공식 홈페이지 | 생성 : {now}")

    return embed

# =================================================================================================================

# 명령어 설정 함수
async def setup(bot : commands.Bot):
    @bot.tree.command(name = "순위", description = "KBO 팀 순위를 확인합니다")

    async def _ranking_command(interaction : discord.Interaction):
        await interaction.response.defer()
        embed = make_ranking_embed()
        await interaction.followup.send(embed = embed)

    print("02. KBO 순위 명령어 로드 완료")