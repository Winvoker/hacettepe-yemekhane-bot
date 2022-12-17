import aiocron
import discord
from discord.ext import tasks, commands
from utils import (
    print_menu,
    update_yemekhane,
    get_date,
    read_token,
    read_channelID,
    read_channelIDs,
)
from database import update_json, add_message, create_db, save_db

intents = discord.Intents.default()
client = discord.Client(intents=intents)


async def send_yemek_message(message):
    if "yarın" in message.content:
        date = get_date(1)
    elif "dün" in message.content:
        date = get_date(-1)
    else:
        date = get_date()

    if date[0] == "0":
        date = date[1:]

    yemekhane = update_yemekhane()

    msg = date + "\n\n"
    msg += print_menu(yemekhane[date])

    await message.channel.send(msg)


@aiocron.crontab("0 20 * * *")
async def auto_send():

    channels = read_channelIDs()
    channels = [await client.fetch_channel(i) for i in channels]

    date = get_date(1)
    if date[0] == "0":
        date = date[1:]

    yemekhane = update_yemekhane()
    update_json(yemekhane)

    msg = date + "\n\n"
    msg += print_menu(yemekhane[date])

    for channel in channels:
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

    if message.content.startswith(".hacettepe sign"):
        new_channel = str(message.channel.id)
        channels = read_channelIDs()

        if new_channel not in channels:
            channels.append(new_channel)

            with open("channel_id", "w") as f:
                for i in channels:
                    f.write(str(i) + "\n")
            await message.channel.send(
                "Kayıt başarılı! Her akşam saat 20:00'da yemek listesi bu kanala atılacak."
            )
            await send_yemek_message(message)

        else:
            await message.channel.send(
                "Bu kanal zaten kayıtlı! Kaydı silmek için .hacettepe unsign komutunu kullanabilirsiniz."
            )
    if message.content.startswith(".hacettepe unsign"):
        channel_to_delete = str(message.channel.id)

        channels = read_channelIDs()
        if channel_to_delete in channels:
            channels.remove(channel_to_delete)

            with open("channel_id", "w") as f:
                for i in channels:
                    f.write(str(i) + "\n")
            await message.channel.send("Kayıt silindi!")
        else:
            await message.channel.send(
                "Bu kanal kayıtlı değil! Kayıt etmek için .hacettepe sign komutunu kullanabilirsiniz."
            )

    if message.content.startswith(".yemek"):
        if "yarın" in message.content:
            date = get_date(1)
        elif "dün" in message.content:
            date = get_date(-1)
        else:
            date = get_date()

        if date[0] == "0":
            date = date[1:]

        yemekhane = update_yemekhane()

        msg = date + "\n\n"
        msg += print_menu(yemekhane[date])

        await message.channel.send(msg)

    if message.content.startswith(".hacettepe"):
        await message.channel.send(
            "Hacettepe Üniversitesi'nin resmi olmayan Discord botu. Yemek listesini görmek için .yemek komutunu kullanabilirsiniz."
        )

    if message.content.startswith(".ceren"):
        await message.channel.send("aka elen tepes. emrenin karısı.")
    if message.content.startswith(".emre"):
        await message.channel.send("aka sei tepes. cerenin kocası.")

    if message.content.startswith(".batu"):
        await message.channel.send("🤙🤙")

    if message.content.startswith(".bobo"):
        await message.channel.send(":flag_tr: :flag_tr:")

    if message.content.startswith(".lülü"):
        await message.channel.send("💖💖 Savaş seni cok seviyomus iletmemi istedi 💖💖")
    if message.content.startswith(".savaş"):
        await message.channel.send("💖💖 Lülü seni cok seviyomus iletmemi istedi 💖💖")

    if message.content.startswith(".sude"):
        await message.channel.send("Lütfen kızma ama tarzını beğenmiyorum.")

    if message.content.startswith(".eda"):
        await message.channel.send("did you mean seda?")

    if message.content.startswith(".mako"):
        await message.channel.send("Merhaba ben 01'liyim. Tanısalım mı?")

    if message.content.startswith(".altar"):
        await message.channel.send("31starwars31")

    if message.content.startswith(".cem"):
        await message.channel.send("Congrats on being tall bro.")

    if message.content.startswith(".guş"):
        await message.channel.send("😔")

    if message.content.startswith(".irem"):
        await message.channel.send("💖 777 manifestliyorum 777 💖")

    if message.content.startswith(".deniz"):
        await message.channel.send("tamamdır 👍")

    if message.content.startswith(".tristy"):
        await message.channel.send("güneşe aşığım")


client.run(read_token())
