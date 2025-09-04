# KBO_Bot

<div align = "center">

![banner](img/discord_banner.png)

</div>

---

## 배포 주소 | Distribution Address

- **초대하기** : [KBO_Bot by Discord](https://discord.com/oauth2/authorize?client_id=1407662854362107934&permissions=8&integration_type=0&scope=bot)

---

## 프로젝트 소개 | Introducion to the Project

```
대한민국의 프로 야구 리그 KBO의 정보를 제공하는 Discord 봇 입니다.
```
> 개발 기간 : 2025.08

---

## 시작 가이드 | Getting start

### 기능 | Function

|명령어|내용|결과|
|:--:|:--:|:--:|
|**/테스트**|봇의 동작 상태를 확인하기 위한 명령어|테스트 완료!|
|**/순위**|현재 KBO 리그 순위 출력을 위한 명령어|🏆 KBO 리그 순위|
|**/일정**|오늘의 KBO 경기 일정을 확인하는 명령어|⚾ 오늘의 KBO 경기 일정|
|**/결과**|오늘의 KBO 경기 결과를 확인하는 명령어|⚾ 오늘의 KBO 경기 결과|

### 요구 사항 | Requirements

**단순 사용 목적**  

```
디스코드에서 봇을 초대하면 바로 사용할 수 있습니다.
별도의 설치나 설정이 필요하지 않습니다.
```

**수정 목적**

- [Python 3.13](https://www.python.org/downloads/)

- [pip Installation]()

```bash
$ pip install discord.py
$ pip install beautifulsoup4
$ pip install selenium
```

---

## 기술 스택 | Tech Stack

![VSC](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)

---

## 개발 일지 | Dev Log

### Version Table

|Version|Description|
|:--:|:--:|
|v1.0|KBO_Bot 생성 & 테스트 명령어 구현 및 기본 정보 크롤링|
|v1.1|순위 & 일정 명령어 구현|
|v1.2|결과 명령어 구현|

### Upcoming Versions

|Version|Description|
|:--:|:--:|
|v1.3|결과 명령어 최적화|

---

## 아키텍쳐 | Architecture

```
📦KBO_Bot
 ┣ 📜README.md
 ┣ 📜LICENSE
 ┃ 
 ┣ 📜KBO_Bot.py
 ┣ 📜KBO_crawler.py
 ┃ 
 ┣ 📜token.json
 ┣ 📜.gitignore
 ┃ 
 ┣ 📂commands
 ┃ ┣ 📜command_ranking.py
 ┃ ┣ 📜command_result.py
 ┃ ┣ 📜command_schedule.py
 ┃ ┣ 📜command_test.py
 ┃ ┗ 📜__init__.py
 ┃ 
 ┣ 📂img
 ┃ ┣ 📜discord_banner.png
 ┃ ┗ 📜SL_emblem.png
 ```