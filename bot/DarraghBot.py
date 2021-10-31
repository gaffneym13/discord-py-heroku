

import os
import discord
import string
import random

TOKEN = os.getenv("DARRAGH_DISCORD_TOKEN")

client = discord.Client()

translator = str.maketrans('', '', string.punctuation)





darragh_quotes = [
    'Eh yeah',
    'Uh huh',
    'Really?',
    'No both those pints are for me',
    'Two Beamish please',
    'Any smokes goin?',
	'Few bav?',
	'Yep',
	'Well if I told you that I\'d have nothing to tell you',
	'That\'s it now',
]




def response_decider(message):
    sentence = message.translate(translator)
    reject = 0
    for word in sentence.split():
        if (word.endswith('er')) & (word != 'er') & (word != 'her') & (word != 'Her')& (word != 'over'):
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

