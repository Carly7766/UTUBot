from discord.ext import commands
from .utils import checks
import discord
import inspect


class ExtensionManager(commands.Cog):
    COG_DIR = 'src.cogs.'

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @checks.is_owner()
    async def load(self, ctx, module: str):
        try:
            self.bot.load_extension(self.COG_DIR + module)
        except Exception as e:
            await ctx.send('\N{NO ENTRY SIGN}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\N{SQUARED OK}')
            await ctx.send('The Extension loaded successfully.')

    @commands.command(hidden=True)
    @checks.is_owner()
    async def unload(self, ctx, module: str):
        try:
            self.bot.unload_extension(self.COG_DIR + module)
        except Exception as e:
            await ctx.send('\N{NO ENTRY SIGN}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\N{SQUARED OK}')
            await ctx.send('The Extension unloaded successfully.')

    @commands.command(hidden=True)
    @checks.is_owner()
    async def reload(self, ctx, module: str):
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send('\N{NO ENTRY SIGN}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\N{SQUARED OK}')


def setup(bot):
    bot.add_cog(ExtensionManager(bot))
