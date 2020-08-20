import discord
from discord.ext import commands

COG_DIR = 'src.cogs.'

INITIAL_COGS = [
    'music',
    'error_handler'
]


class UTUBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)

        for cog in INITIAL_COGS:
            self.load_extension(COG_DIR + cog)

    async def on_ready(self):
        game = discord.Game("UTUBot Ver:0.1a")
        await self.change_presence(status=discord.Status.online, activity=game)
        self.description = "HogeHoges"

        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')
