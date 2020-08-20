import discord
import sys
from discord.ext import commands


class MusicCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play', aliases=['p'])
    async def play(self, ctx):
        await ctx.send("hoge")


def setup(bot):
    bot.add_cog(MusicCog(bot))
