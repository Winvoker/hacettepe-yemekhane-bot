import json
import requests
import xmltodict
import datetime
from datetime import timedelta


def get_date(after=0):
    today = datetime.datetime.now()
    today = today + timedelta(days=after)
    today = today + timedelta(hours=3)
    return today.strftime("%d.%m.%Y")


def read_token():
    with open("DISCORD_TOKEN", "r") as f:
        return f.readline()


def read_channelID():
    with open("channel_id", "r") as f:
        return f.readline()


def print_menu(menu):
    string_to_send = ""
    for i in menu[0]:
        string_to_send += "• " + i + "\n"
    string_to_send += "Kalori:" + menu[1]
    return string_to_send


def update_yemekhane():
    url = "http://www.sksdb.hacettepe.edu.tr/YemekListesi.xml"
    response = requests.get(url)
    data = xmltodict.parse(response.content)
    data = data["gunler"]["gun"]
    yemekhane = {}
    for i in data:
        tarih = i["tarih"].split()[0]
        yemekler = i["yemekler"]["yemek"]
        kalori = i["kalori"]
        yemekhane[tarih] = [yemekler, kalori]
    return yemekhane
