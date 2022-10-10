import aiocron
import discord
from discord.ext import tasks, commands
from utils import print_menu, update_yemekhane, get_date, read_token, read_channelID
from database import update_json, add_message, create_db, save_db

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@aiocron.crontab("0 12 * * *")
async def auto_send():
    channel = await client.fetch_channel(read_channelID())
    date = get_date(1)
    if date[0] == "0":
        date = date[1:]

    yemekhane = update_yemekhane()
    update_json(yemekhane)

    msg = date + "\n\n"
    msg += print_menu(yemekhane[date])

    await channel.send(msg)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    auto_send.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot == True:
        return

    if message.content.startswith(".yemek"):
        if "yarın" in message.content:
            date = get_date(1)
        elif "dün" in message.content:
            date = get_date(-1)
        else:
            date = get_date()

        if date[0] == "0":
            date = date[1:]

        print(message)
        print(date)
        yemekhane = update_yemekhane()

        msg = date + "\n\n"
        msg += print_menu(yemekhane[date])

        await message.channel.send(msg)


client.run(read_token())
