import discord
# print(discord.__version__)
intents = discord.Intents.default()
# intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#'):
        await message.channel.send('My name is Stephon!')

client.run('OTk0MjMzODE1NTExODcxNTc5.Gn8vvG.u855DtyTfgTbuvHYhWiF9nSZcsYsJ8I4GSCOcQ')