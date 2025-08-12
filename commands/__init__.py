# 새로운 명령어 파일 추가할 때마다 여기에 추가
from .command_test import setup as setup_test
from .command_ranking import setup as setup_kbo_ranking

# 모든 setup 함수들을 리스트로 관리
async def load_all_commands(bot):
    # 모든 명령어 모듈을 한 번에 로드
    await setup_test(bot)
    await setup_kbo_ranking(bot)

    print("=====================================")
    print("모든 명령어 모듈 로드 완료")
    print("=====================================")