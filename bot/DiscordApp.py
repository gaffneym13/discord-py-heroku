import os
import discord
from dotenv import load_dotenv
import nest_asyncio
import random
import string


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()

translator = str.maketrans('', '', string.punctuation)


def response_decider(message):
    sentence = message.translate(translator)
    for word in sentence.split():
        if word.endswith('er') :
            response = word.title() + '? I barely knew her!'
            return(response)
        if word.endswith('im') :
            response = word.title() + '? I barely knew him!'
            return(response)
    return



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = response_decider(message.content)
    if response is not None:
        await message.channel.send(response)
        response = None

client.run(TOKEN)