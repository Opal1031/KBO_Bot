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

## 시작 가이드 및 요구 사항 | Getting start & Requirements

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