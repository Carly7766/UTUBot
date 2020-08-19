import discord
import sys
from discord.ext import commands


class MusicCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        @bot.command()
    @commands.before_invoke(record_usage)
    async def who(ctx): # Output: <User> used who at <Time>
    await ctx.send('i am a bot')

    @commands.command(name='play', aliases=['p'])
    async def play(self, ctx):
        await ctx.send("hoge")


def setup(bot):
    bot.add_cog(MusicCog(bot))
