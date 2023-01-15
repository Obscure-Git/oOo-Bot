import discord, json, requests, aiohttp, randfacts

from discord.ext import commands
from aiohttp import request

apierror = discord.Embed(
                    description = f"<a:a_cross:778982620347498496> ***An API error occured!***" ,
                    color= discord.Color.from_rgb(240, 73, 71)
)

no_color = discord.Color.from_rgb(47, 49, 54)

class facts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['facts'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def fact(self, ctx, animal = None):

        if animal == None:

            try:
                fact = randfacts.getFact()

            except:
                await ctx.send(embed = apierror)
                return

            embed = discord.Embed(description = f"{fact}", color = no_color)
            embed.set_footer(text = "Source: RandFacts")

            try:
                await ctx.send(embed = embed)

            except:
                try:
                    await ctx.send(fact)

                except:
                    await ctx.send(embed = apierror)


        elif (animal.lower()) in ("dog", "cat", "panda", "fox", "bird", "koala"):
            fact_url = f"https://some-random-api.ml/facts/{animal}"

            if animal == "bird":
                animal = "birb"
            else:
                animal = animal

            image_url = f"https://some-random-api.ml/img/{animal}"

            async with request("GET", image_url, headers = {}) as response:
                if response.status == 200:
                    data = await response.json()
                    image_link = data["link"]

                else:
                    image_link = None

            if animal == "birb":
                animal = "bird"

            async with request("GET", fact_url) as response:
                if response.status == 200:
                    data = await response.json()

                    try:
                        embed = discord.Embed(title = f"{animal.title()} Fact" , description = f"{data['fact']}", color = no_color)

                        embed.set_footer(text=f"Source : Some-Random-API")

                    except:
                        await ctx.send("An error occured while sending embed. Make sure that I have `embed links` permissions.")

                    if image_link is not None:
                        embed.set_image(url = image_link)

                    await ctx.send(embed = embed)

                else:
                    try:
                        await ctx.send(embed = apierror)

                    except:
                        await ctx.send(f"Api returned an error!\nResponse Status : `{response.status}`")

        else:
            await ctx.send("No facts found for that animal.\nCurrently supported animals are : `dog`, `cat`, `panda`, `fox`, `bird`, `koala`.")

def setup(bot):
    bot.add_cog(facts(bot))
