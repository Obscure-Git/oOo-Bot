import discord
from discord.ext import commands

class onready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(
        """
-----------------------------------------------
--------------------READY----------------------
-----------------------------------------------
        """
    )

        channel = await self.bot.fetch_channel(774308134448660570)
        await channel.send("Ready")

def setup(bot):
    bot.add_cog(onready(bot))