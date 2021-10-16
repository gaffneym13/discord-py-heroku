#!/usr/bin/env python
# coding: utf-8

# In[1]:


# bot.py
import os
import discord
from dotenv import load_dotenv
import nest_asyncio
import random
import string


# In[2]:


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


# In[3]:


translator = str.maketrans('', '', string.punctuation)


# In[4]:


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


# In[ ]:


nest_asyncio.apply()
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = response_decider(message.content)
    if response is not None:
        await message.channel.send(response)
        response = None

client.run(TOKEN)