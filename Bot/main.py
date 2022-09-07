import asyncio
import nextcord
from nextcord import Interaction
import discord
import re
import deez as d
import diceroller
import foodIdeas
import config

token = config.token
test_server_id = 899004736274055208
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.slash_command(name = "deez", description = "deez nuts joke game", guild_ids = [test_server_id])
async def deez(interaction: Interaction):
  prompt = d.prompt()
  #prompt = d.prompt_test()

  sent = await interaction.response.send_message(prompt['prompt'])
  sent = await sent.fetch()
  await sent.add_reaction('🥜')
  await sent.add_reaction('❌')

  def check(reaction, user):
    '''#is a joke
    if prompt['reply']['second'] != '':
      if user == interaction.user and str(reaction.emoji) == '🥜':
        return True

      elif user == interaction.user and str(reaction.emoji) == '❌':
        return True

      else:
        return False

    else:
      if user == interaction.user and str(reaction.emoji) == '❌':
        return True

      elif user == interaction.user and str(reaction.emoji) == '🥜':
        return True

      else:
        return False'''

    return user == interaction.user and (str(reaction.emoji) == '🥜' or str(reaction.emoji) == '❌')

  try:
    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)

  except asyncio.TimeoutError:
    await interaction.followup.send('Timer expired.')

  else:
    #Is a joke
    if prompt['reply']['second'] != '':

      if str(reaction) == '🥜':
        await interaction.followup.send('Nice Job, it was a deez nuts joke! \n' + 'Punchline: ' + prompt['reply']['second'])

      else:
        await interaction.followup.send(d.j_response() + '\n' + 'Punchline: ' + prompt['reply']['second'])

    #Not a joke, X is correct and ✅ is incorrect
    else:
      if str(reaction) == '❌':
        await interaction.followup.send('Nice Job, it was not a deez nuts joke!')
      else:
        await interaction.followup.send(d.nj_response())


@client.event
async def on_message(message):
  # checks whether the author of the message is the bot, don't want to reply to self.
  if message.author == client.user:
    return
    # checks for specific author id

  '''if message.author.id == 100344908467961856:
    #adds reaction, arg must be valid UNICODE
    await message.add_reaction('😈')'''

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

  '''elif message.content.startswith("/deez"):
    prompt = d.prompt()
    sent = await message.channel.send(prompt['prompt'])
    await sent.add_reaction('😈')
    await sent.add_reaction('❌')

    def check(reaction, user):
      return user == message.author and (str(reaction.emoji) == '😈' or sent.add_reaction('❌'))

    try:
      reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)

    except asyncio.TimeoutError:
      await message.channel.send('Timer expired.')

    else:
      await message.channel.send(prompt['reply']['second'])'''


client.run(token)