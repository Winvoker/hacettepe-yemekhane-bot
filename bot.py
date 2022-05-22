from discord.ext import tasks, commands
import discord
from utils import print_menu, update_yemekhane, get_date, read_token, read_channelID

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@tasks.loop(hours=24.0)
async def auto_send():
    channel = await client.fetch_channel(read_channelID())
    date = get_date(1)

    print(date)
    yemekhane = update_yemekhane()

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

    if message.content.startswith(".yemek"):
        if "yarın" in message.content:
            date = get_date(1)
        elif "dün" in message.content:
            date = get_date(-1)
        else:
            date = get_date()
        print(message)
        print(date)
        yemekhane = update_yemekhane()

        msg = date + "\n\n"
        msg += print_menu(yemekhane[date])

        await message.channel.send(msg)


client.run(read_token())
