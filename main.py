import discord
import os
from src import utubot

token = os.getenv('BOT_TOKEN')
prefix = os.getenv('PREFIX')

bot = utubot.UTUBot(prefix)

bot.run(token)
