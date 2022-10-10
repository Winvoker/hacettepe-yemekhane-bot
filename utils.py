import json
import requests
import xmltodict
import datetime
from datetime import timedelta
from database import update_json


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


def read_channelIDs():

    with open("channel_id", "r") as f:
        channel_ids = f.readlines()
    channel_ids = [i.strip("\n") for i in channel_ids]

    return channel_ids


def print_menu(menu):
    string_to_send = ""
    for i in menu[0]:
        string_to_send += "• " + i + "\n"
    string_to_send += "\nKalori : " + menu[1]
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
    updated_json = update_json(yemekhane)
    return updated_json
