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
  msg = message.content.lower()
  if "cum" == msg:
    if os.path.exists("disabled.txt"):
      await message.reply("*Wtf bro im already cummed*")
      return
    with open('disabled.txt', 'w'):
      pass
    await message.reply("Mmmmmm\n*Mouth is full*")
  if "uncum" == msg:
    os.remove('disabled.txt')
    await message.reply("*Swallowed*")
  await bot.process_commands(message)

@bot.event
async def on_message_edit(before, after):
  await _message_edit(before, after)
  await bot.process_commands(after)
  
bot.run(os.environ['TOKEN'])
