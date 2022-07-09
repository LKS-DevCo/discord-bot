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

    # Deletes number of messages specified by user after lks delete prefix is detected
    if message.content.startswith(delete):
        full_string = message.content
        delete_num = full_string.removeprefix(delete)

        # Convert to int to be used in argument for purging
        delete_num = int(delete_num)

        # Get channel name
        channel_name = str(message.channel)
        c_channel = discord.utils.get(message.guild.text_channels, name=channel_name)
        await message.delete()
        await c_channel.purge(limit=delete_num)

client.run(TOKEN)
