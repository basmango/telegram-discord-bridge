import discord
import os
import threading
import asyncio
from botIPC import async_connect
BLACK_LIST = []
TOKEN = os.getenv('D_TOKEN')
GUILD = os.getenv('G_TOKEN')
CHANNEL_NAME = os.getenv("CHANNEL_NAME")
client = discord.Client()
sock = ""


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    global sock
    sock = await async_connect()
    await main(sock)


@client.event
async def on_message(message):
    if message.author == client.user or message.content == "":
        return

    channel = message.channel.name
    if channel in BLACK_LIST:
        return
    message_string = '[' + channel+']'  + \
        "<*" + message.author.name + "*> "+message.content

    dispatched = [message_string.encode("UTF-8")]

    await sock.send_multipart(dispatched)


async def send_message(mesg, chnl):

    await chnl.send(mesg)


async def main(sock):
    main_channel = discord.utils.get(client.get_all_channels(), name=CHANNEL_NAME)
    while True:
        from_telegram = await sock.recv_multipart()

        from_telegram = from_telegram[0].decode("UTF-8")
        await send_message(from_telegram, main_channel)


client.run(TOKEN)
