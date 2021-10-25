

import os
import discord
import string
import random

TOKEN = os.getenv("DARRAGH_DISCORD_TOKEN")

client = discord.Client()

translator = str.maketrans('', '', string.punctuation)





darragh_quotes = [
    '/tts Eh yeah',
    '/tts Uh huh',
    '/tts Really?',
    '/tts No both those pints are for me',
    '/tts Two Beamish please',
    '/tts Any smokes goin?',
	'/tts Few bav?',
	'/tts Yep',
	'/tts Well if I told you that I\'d have nothing to tell you',
	'/tts That\'s it now',
]




def response_decider(message):
    sentence = message.translate(translator)
    reject = 0
    for word in sentence.split():
        if (word.endswith('er')) & (word != 'er') & (word != 'her') & (word != 'over'):
            reject = 1 
        if (word.endswith('im')) & (word != 'im') & (word != 'him'):
            reject = 1 
    
    if reject == 0:
        response = random.choice(darragh_quotes)
        return response
    else:
        return




@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if random.sample(range(1,5), 1)[0] != 1:
        return

    response = response_decider(message.content)
    if response is not None:
        await message.channel.send(response)
        response = None

client.run(TOKEN)

