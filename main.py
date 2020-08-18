import discord
import os
from src import UTUBot

token = os.getenv('BOT_TOKEN')
prefix = os.getenv('PREFIX')

bot = UTUBot.UTUBot(prefix)

bot.run(token)
