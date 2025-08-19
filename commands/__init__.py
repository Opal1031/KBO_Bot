from .command_test import setup as setup_test
from .command_ranking import setup as setup_kbo_ranking
from .command_schedule import setup as setup_kbo_schedule

async def load_all_commands(bot):
    await setup_test(bot)
    await setup_kbo_ranking(bot)
    await setup_kbo_schedule(bot)

    print("=====================================")
    print("모든 명령어 모듈 로드 완료")
    print("=====================================")