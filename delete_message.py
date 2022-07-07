import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()

client = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

prefix = "lks"
delete = "lks delete"


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'The token is: {TOKEN}')
    print(f'The guild is: {GUILD}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == prefix:
        await message.channel.send("HELP REPLY")
    # TODO: Should send help reply showing what can be done with bot

    if message.content.startswith(delete):
        # TODO: Assign as int type and request that many messages be delete + 1 (includes the bot message)
        full_string = message.content
        delete_num = full_string.removeprefix(delete)
        await message.channel.send('deleting....' + delete_num)
        await message.delete()  # deletes message that was typed by user
        # TODO: Delete messages before this as well


    if message.content.startswith('$name'):
        await message.channel.send(GUILD)


client.run(TOKEN)
