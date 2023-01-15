import discord, aiohttp, random, json

from aiohttp import request
from random import randint
from discord.ext import commands

api_creds = "Source: Nekobot API"
tweet_color = discord.Color.from_rgb(76, 154, 229) 
no_color = discord.Color.from_rgb(47, 49, 54)



class meme_actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["whowouldwin", "www", "vs"])
    async def versus(self, ctx, user1: discord.Member, user2: discord.Member):

        img_url1 = user1.avatar_url
        img_url2 = user2.avatar_url

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={img_url1}&user2={img_url2}") as r:
                res = await r.json()

                image = res['message']

                e = discord.Embed(title = f"Who would win?", description = f"{user1.mention} VS {user2.mention}", color = no_color)

                e.set_image(url = image)
                e.set_footer(text = api_creds)

                msg = await ctx.send(embed = e)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣")

    @commands.command()
    async def ship(self, ctx, user1: discord.Member, user2: discord.Member):

        img_url1 = user1.avatar_url
        img_url2 = user2.avatar_url

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=ship&user1={img_url1}&user2={img_url2}") as r:
                res = await r.json()

                image = res['message']

                e = discord.Embed(title = f" ", description = f"{ctx.author.mention} shipped {user1.mention}  with {user2.mention}", color = no_color)

                e.set_image(url = image)
                e.set_footer(text = api_creds)

                await ctx.send(embed = e)

    @commands.command()
    async def tweet(self, ctx, username, *, text = None):
        characters = len(text)

        if characters > 70:
            await ctx.send("Your text should be under 70 characters!")

        elif text == None:
            await ctx.send("Tweets cant be empty!")

        else:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username={username}") as r:
                    res = await r.json()

                    image = res['message']

                    e = discord.Embed(color = tweet_color)

                    e.set_image(url = image)
                    e.set_footer(text = api_creds)

                    await ctx.send(embed = e)


    @commands.command()
    async def trumptweet(self, ctx, *, text = None):

        characters = len(text)

        if characters > 70:
            await ctx.send("Your text should be under 70 characters!")

        elif text == None:
            await ctx.send("Tweets cant be empty!")

        else:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}") as r:
                    res = await r.json()

                    image = res['message']

                    e = discord.Embed(color = tweet_color)

                    e.set_image(url = image)
                    e.set_footer(text = api_creds)
                    await ctx.send(embed = e)



    @commands.command()
    async def trash(self, ctx, user: discord.Member):

        img_url = user.avatar_url

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=trash&url={img_url}") as r:
                res = await r.json()

                image = res['message']
                
                e = discord.Embed(color = no_color)

                e.set_image(url = image)
                e.set_footer(text = api_creds)

                await ctx.send(embed = e)

    @commands.command(aliases = ['bread'])
    async def baguette(self, ctx, user: discord.Member):

        img_url = user.avatar_url

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=baguette&url={img_url}") as r:
                res = await r.json()

                image = res['message']
                
                e = discord.Embed(color = no_color)

                e.set_image(url = image)
                e.set_footer(text = api_creds)

                await ctx.send(embed = e)


    @commands.command()
    async def awooify(self, ctx, user: discord.Member):

        img_url = user.avatar_url

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=awooify&url={img_url}") as r:
                res = await r.json()

                image = res['message']
                
                e = discord.Embed(color = no_color)

                e.set_image(url = image)
                e.set_footer(text = api_creds)

                await ctx.send(embed = e)


    @commands.command(aliases = ['iphonex'])
    async def iphone(self, ctx, user: discord.Member):

        if user == None:
            img_url = ctx.author.avatar_url
        
        else:
            img_url = user.avatar_url

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={img_url}") as r:
                res = await r.json()

                image = res['message']
                
                e = discord.Embed(color = no_color)

                e.set_image(url = image)
                e.set_footer(text = api_creds)

                await ctx.send(embed = e)

    @commands.command(aliases = ["changemymind"])
    async def cmm(self, ctx, *, text = None):

        characters = len(text)

        if characters > 70:
            await ctx.send("Your text should be under 70 characters!")

        elif text == None:
            await ctx.send("Nothing?")

        else:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}") as r:
                    res = await r.json()

                    image = res['message']

                    e = discord.Embed(color = no_color)

                    e.set_image(url = image)
                    e.set_footer(text = api_creds)

                    await ctx.send(embed = e)

def setup(bot):
    bot.add_cog(meme_actions(bot))