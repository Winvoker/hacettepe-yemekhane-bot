# Hacettepe Yemekhane Bot

This discord bot shows which foods will be served at Hacettepe dining hall.

You can add to your server. [link](https://discord.com/oauth2/authorize?client_id=966733779647471686&permissions=2048&scope=bot)

## How to use bot
* .yemek : Gives list of today's menu.
* .yemek yarın : Gives list of tommorow's menu.
* .yemek dün : Gives list of yesterday's menu.
* .hacettepe sign : Sign spesific channel to get automated messages every day at 20:00. 
* .hacettepe unsign : Unsign channel
## Getting Started

### Dependencies

* discord.py
* xmltodict

### Installing

* Clone repo
* Install dependencies
```
pip install -r requirements.txt
```
* Get your discord token from discord [developer portal](https://discord.com/developers/)
* Create file named DISCORD_TOKEN without extension.
* Paste your token into file

### Executing program

```
python bot.py
```

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details

## TO-DO:
* ~~Make automatic announcement without calling with a command (.yemek)~~
* ~~Write a signing system which users use a .kayit command to set a channel for automatic announcements.~~
* Create docker image
* Auto deploy on aws upon push.

All pull requests are welcome ! Please use flake8 and black before PR.
