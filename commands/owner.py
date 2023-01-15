import discord
from discord.ext import commands

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):

        extension = extension.lower()

        if extension == "owner":
            return

        try:

            self.bot.load_extension(f"events.{extension}")
            await ctx.send(f"{extension} events loaded")

        except:
            try:
                self.bot.load_extension(f"commands.{extension}")
                await ctx.send(f"{extension} commands unloaded")

            except:
                await ctx.send(f"An error occured!")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):

        extension = extension.lower()

        if extension == "owner":
            return

        try:
            self.bot.unload_extension(f"events.{extension}")
            await ctx.send(f"{extension} events unloaded")

        except:
            try:
                self.bot.unload_extension(f"commands.{extension}")
                await ctx.send(f"{extension} commands unloaded")
            
            except:
                await ctx.send(f"An error occured!")

    @commands.command()
    @commands.is_owner()
    async def load_sub(self, ctx, extension):

        extension = extension.lower()

        if extension == "owner":
            return

        try:

            self.bot.load_extension(f"commands.actions.{extension}")
            await ctx.send(f"{extension} events loaded")

        except:
            try:
                self.bot.load_extension(f"commands.fun.{extension}")
                await ctx.send(f"{extension} commands unloaded")

            except:
                await ctx.send(f"An error occured!")

    @commands.command()
    @commands.is_owner()
    async def unload_sub(self, ctx, extension):

        extension = extension.lower()

        if extension == "owner":
            return

        try:

            self.bot.unload_extension(f"commands.actions.{extension}")
            await ctx.send(f"{extension} events loaded")

        except:
            try:
                self.bot.unload_extension(f"commands.fun.{extension}")
                await ctx.send(f"{extension} commands unloaded")

            except:
                await ctx.send(f"An error occured!")


    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):

        extension = extension.lower()

        if extension == "owner":
            return

        try:
            self.bot.unload_extension(f"events.{extension}")
            await ctx.send(f"{extension} events unloaded.")
            self.bot.load_extension(f"events.{extension}")
            await ctx.send(f"{extension} events loaded.")

        except:
            try:
                self.bot.unload_extension(f"commands.{extension}")
                await ctx.send(f"{extension} commands unloaded.")
                self.bot.load_extension(f"commands.{extension}")
                await ctx.send(f"{extension} commands loaded.")
            
            except:
                await ctx.send(f"An error occured!")

    @commands.command()
    @commands.is_owner()
    async def guilds(self, ctx, num: int):

        guilds = self.bot.guilds

        for guild in guilds:
            guild = self.bot.get_guild(guild.id)
            
            channel = guild.channels[num]
            
            name = guild.name

            invite = await channel.create_invite(max_uses=5)
            
            await ctx.send(f"{name}: {invite}")

def setup(bot):
    bot.add_cog(owner(bot))