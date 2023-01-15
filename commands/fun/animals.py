import discord, json, random, requests, aiohttp, randfacts

from discord.ext import commands
from aiohttp import request

apierror = discord.Embed(
                    description = f"<a:a_cross:778982620347498496> ***An API error occured!***" ,
                    color= discord.Color.from_rgb(240, 73, 71)
)

no_color = discord.Color.from_rgb(47, 49, 54)


class animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # cats
    @commands.command(aliases=["cats", 'meow', 'meo'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cat(self, ctx):

        r = requests.get(f"https://api.thecatapi.com/v1/images/search")

        json = r.json()
        img = json[0]["url"]

        if r.status_code == 200:
            embed = discord.Embed(description = " ", color= no_color)

            embed.set_image(url = img)

            embed.set_footer(text=f"Source: thecatapi.com")

            return await ctx.send(embed = embed)

        else:

            return await ctx.send(embed = apierror)

    # dogs
    @commands.command(aliases=["dogs", 'woof', 'bow'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, ctx):

        r = requests.get("https://random.dog/woof.json")

        json = r.json()
        img = json["url"]

        if r.status_code == 200:
            sdog = discord.Embed(description=" ", color= no_color)

            sdog.set_image(url = img)

            sdog.set_footer(text=f"Source: random.dog")
            return await ctx.send(embed=sdog)

        else:
            return await ctx.send(embed = apierror)

def setup(bot):
    bot.add_cog(animals(bot))