# This example requires the 'message_content' intent.

import discord
from utils import print_menu, update_yemekhane, get_date

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(".yemek") or message.content.startswith(".y"):
        if "yarın" in message.content:
            date = get_date(1)
        elif "dün" in message.content:
            date = get_date(-1)
        else:
            date = get_date()

        yemekhane = update_yemekhane()

        msg = date + " tarihli yemek listesi:\n\n"
        msg += print_menu(yemekhane[date])

        await message.channel.send(msg)


client.run("token")  #
