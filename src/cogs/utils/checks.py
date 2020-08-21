from discord.ext import commands
import discord.utils


def is_owner():
    async def predicate(ctx):
        return ctx.author.id == 384662299887009793
    return commands.check(predicate)