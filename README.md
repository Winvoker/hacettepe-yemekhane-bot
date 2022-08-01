# Hacettepe Yemekhane Bot

This discord bot shows which foods will be served at Hacettepe dining hall.

## How to use bot
* .yemek : Gives list of today's menu.
* .yemek yarın : Gives list of tommorow's menu.
* .yemek dün : Gives list of yesterday's menu.
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
* Create docker image
* Auto deploy on aws upon push.

All pull requests are welcome ! Please use flake8 and black before PR.
