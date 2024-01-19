from cogs import command, vars
from cogs.message import _message
from cogs.message_edit import _message_edit
import discord
import os
from cogs.vars import *

bot = command.bot

@bot.event
async def on_message(message):
  if not os.path.exists("disabled.txt"):
    await _message(message)
    await bot.process_commands(message)
  msg = message.content.lower()
  if "cum" == msg:
    with open('disabled.txt', 'w'):
      pass
  if "uncum" == msg:
    os.remove('disabled.txt')

@bot.event
async def on_message_edit(before, after):
  await _message_edit(before, after)
  await bot.process_commands(after)
  
bot.run(os.environ['TOKEN'])
