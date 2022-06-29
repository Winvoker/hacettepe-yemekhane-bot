from discord.ext import tasks, commands
import discord
from utils import print_menu, update_yemekhane, get_date, read_token, read_channelID
from database import update_json, add_message, create_db, save_db

intents = discord.Intents.default()
client = discord.Client(intents=intents)

ignored_channels = [
    "928275152830103623",
    "933765068183728180",
    "934464950817132554",
    "922518769459429396"
]

global db, db_bot

db = create_db()
db_bot = create_db()

@tasks.loop(hours=24.0)
async def auto_send():
    channel = await client.fetch_channel(read_channelID())
    date = get_date(1)
    if date[0] == '0':
        date = date[1:]
    
    print(date)
    yemekhane = update_yemekhane()
    update_json(yemekhane)

    msg = date + "\n\n"
    msg += print_menu(yemekhane[date])

    await channel.send(msg)

@tasks.loop(hours=24.0)
async def auto_save_db():
    global db, db_bot
    save_db(db)
    db = create_db()

    save_db(db_bot)
    db_bot = create_db()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    auto_save_db.start()
    auto_send.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot == True:
        return

    if message.channel.id not in ignored_channels:
        add_message(db, message)
    else:
        add_message(db_bot, message)

    if message.content.startswith(".yemek"):
        if "yarın" in message.content:
            date = get_date(1)
        elif "dün" in message.content:
            date = get_date(-1)
        else:
            date = get_date()

        if date[0] == '0':
            date = date[1:]
        
        print(message)
        print(date)
        yemekhane = update_yemekhane()

        msg = date + "\n\n"
        msg += print_menu(yemekhane[date])

        await message.channel.send(msg)

client.run(read_token())