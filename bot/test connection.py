import os
import discord




TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()

translator = str.maketrans('', '', string.punctuation)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")




@client.event
async def on_message(message):
    if message.author == client.user:
        return


client.run(TOKEN)