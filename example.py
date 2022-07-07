# This example requires the 'message_content' intent.
import os
import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
# intents.message_content = True

client = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'The token is: {TOKEN}')
    print(f'The guild is: {GUILD}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$token'):
        await message.channel.send(TOKEN)

    if message.content.startswith('$name'):
        await message.channel.send(GUILD)


client.run(TOKEN)
