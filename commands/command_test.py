import discord
from discord.ext import commands

# =================================================================================================================

# 명령어 설정 함수
async def setup(bot : commands.Bot):
    @bot.tree.command(name = "테스트", description = "테스트 명령어입니다")
    async def _command_test(interaction : discord.Interaction):
        await interaction.response.send_message("테스트 완료!")

    print("01. test 명령어 로드 완료")