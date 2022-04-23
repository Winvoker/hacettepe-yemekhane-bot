import requests
import xmltodict
from datetime import date, timedelta


def get_date(after=0):
    today = date.today()
    today += timedelta(days=after)
    return today.strftime("%d.%m.%Y")


string_to_send = ""
print(get_date())


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
