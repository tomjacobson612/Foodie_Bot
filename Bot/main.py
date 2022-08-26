import discord
import re
#import os
import diceroller
import foodIdeas
import config

token = config.token
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  # checks whether the author of the message is the bot, don't want to reply to self.
  if message.author == client.user:
    return
    # checks for specific author id

  """if message.author.id == 100344908467961856:
    #adds reaction, arg must be valid UNICODE
    await message.add_reaction('😈')"""

  # if message starts with '$hello', then send 'Hello!'
  if message.content.startswith("!hello"):
    await message.channel.send("Hello!")

  # uses regex to search message.content for "Paul", ignoring case
  # Regex string 'Paul', exact match only r'\b(Paul)\b''
  elif re.search(r'\b(Paul)\b', message.content, re.IGNORECASE):
    await message.channel.send("Shut up Paul!")

  # diceroll command
  elif re.search(r'^[!][0-9]{1,5}?[d][0-9]{1,5}?$', message.content):
    await message.channel.send(diceroller.parse_roll(message.content))

  elif message.content.startswith("!food"):
    await message.channel.send(foodIdeas.random_food())


client.run(token)