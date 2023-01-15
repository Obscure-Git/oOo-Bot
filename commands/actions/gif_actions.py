import discord, json, aiohttp, random, requests, os

from discord.ext import commands
from aiohttp import request
from random import randint

### This Actions file has action commands that pull images from tenor api ###

key = os.environ['Tenor']

bot_stuff = {
    "success": discord.Color.from_rgb(67, 180, 129),
    "fail": discord.Color.from_rgb(240, 73, 71),
    "none": discord.Color.from_rgb(47, 49, 54),
    "support": "https://discord.gg/s2khsve",
    "botinv": "https://discord.com/oauth2/authorize?client_id=772818044933242880&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2Finvite%2Fs2khsve&scope=bot",
    "website": "https://obot.netlify.app/",
    "owner": "Obscure#6969"
}

class gif_actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def punch(self, ctx, *, user: discord.Member = None):
        if user == None:
            return await ctx.send("Who do you wanna punch?")

        if user == ctx.author:
            return await ctx.send("You cant punch yourself.")

        else:
            msg = f"{ctx.author.mention} punched {user.mention}!"

        query = "anime punch"

        search = f"https://api.tenor.com/v1/random?q={query}&key={key}&limit=1&media_filter=basic"
        get = requests.get(search)
        
        if get.status_code == 200:
            json_search = get.json()
            json_check = json_search['next']

            if json_check == "0":
                await ctx.message.channel.send("I didn't found any gifs")

            else:
                try:
                    json_s = json_search['results']
                    
                    image = json_s[0]
                    image = image.get("media")
                    image = image[0]
                    image = image.get("gif")
                    image = image.get("url")


                    embed = discord.Embed(description = msg, color = bot_stuff['none'])

                    embed.set_image(url = image)
                    embed.set_footer(text = f"Source: Tenor")

                    await ctx.message.channel.send(embed=embed)

                except:
                    await ctx.send("Search Term was not valid.")
        
        elif get.status_code == 404:
            await ctx.message.channel.send("404 error")
        
        elif get.status_code == 403:
            await ctx.message.channel.send('403 forbidden error')
        
        else:
            await ctx.send("An Error Occured")

    @commands.command()
    async def slap(self, ctx, *, user: discord.Member = None):

        if user == None:
            return await ctx.send("Who do you wanna slap?")

        if user == ctx.author:
            return await ctx.send("You cant slap yourself.")

        else:
            msg = f"{ctx.author.mention} slapped {user.mention}!"
            
        query = "anime slap"

        search = f"https://api.tenor.com/v1/random?q={query}&key={key}&limit=1&media_filter=basic"
        get = requests.get(search)
        
        if get.status_code == 200:
            json_search = get.json()
            json_check = json_search['next']

            if json_check == "0":
                await ctx.message.channel.send("I didn't found any gifs")

            else:
                try:
                    json_s = json_search['results']
                    
                    image = json_s[0]
                    image = image.get("media")
                    image = image[0]
                    image = image.get("gif")
                    image = image.get("url")


                    embed = discord.Embed(description = msg, color = bot_stuff['none'])

                    embed.set_image(url = image)
                    embed.set_footer(text = f"Source: Tenor")

                    await ctx.message.channel.send(embed=embed)

                except:
                    await ctx.send("Search Term was not valid.")
        
        elif get.status_code == 404:
            await ctx.message.channel.send("404 error")
        
        elif get.status_code == 403:
            await ctx.message.channel.send('403 forbidden error')
        
        else:
            await ctx.send("An Error Occured")

    @commands.command()
    async def poke(self, ctx, *, user: discord.Member = None):

        if user == None:
            return await ctx.send("Who do you wanna poke?")
        
        if user == ctx.author:
            return await ctx.send("You cant poke yourself.")
        
        else:
            msg = f"{ctx.author.mention} is poking {user.mention}!"
            
        query = "anime poking"

        search = f"https://api.tenor.com/v1/random?q={query}&key={key}&limit=1&media_filter=basic"
        get = requests.get(search)
        
        if get.status_code == 200:
            json_search = get.json()
            json_check = json_search['next']

            if json_check == "0":
                await ctx.message.channel.send("I didn't found any gifs")

            else:
                try:
                    json_s = json_search['results']
                    
                    image = json_s[0]
                    image = image.get("media")
                    image = image[0]
                    image = image.get("gif")
                    image = image.get("url")


                    embed = discord.Embed(description = msg, color = bot_stuff['none'])

                    embed.set_image(url = image)
                    embed.set_footer(text = f"Source: Tenor")

                    await ctx.message.channel.send(embed=embed)

                except:
                    await ctx.send("Search Term was not valid.")
        
        elif get.status_code == 404:
            await ctx.message.channel.send("404 error")
        
        elif get.status_code == 403:
            await ctx.message.channel.send('403 forbidden error')
        
        else:
            await ctx.send("An Error Occured")


    @commands.command()
    async def bonk(self, ctx, *, user: discord.Member = None):

        if user == None:
            return await ctx.send("Who do you wanna bonk?")

        if user == ctx.author:
            return await ctx.send("You cant bonk yourself.")

        else:
            msg = f"{ctx.author.mention} bonked {user.mention}!"
            
        query = "bonk"

        search = f"https://api.tenor.com/v1/random?q={query}&key={key}&limit=1&media_filter=basic"
        get = requests.get(search)
        
        if get.status_code == 200:
            json_search = get.json()
            json_check = json_search['next']

            if json_check == "0":
                await ctx.message.channel.send("I didn't found any gifs")

            else:
                try:
                    json_s = json_search['results']
                    
                    image = json_s[0]
                    image = image.get("media")
                    image = image[0]
                    image = image.get("gif")
                    image = image.get("url")


                    embed = discord.Embed(description = msg, color = bot_stuff['none'])

                    embed.set_image(url = image)
                    embed.set_footer(text = f"Source: Tenor")

                    await ctx.message.channel.send(embed=embed)

                except:
                    await ctx.send("Search Term was not valid.")
        
        elif get.status_code == 404:
            await ctx.message.channel.send("404 error")
        
        elif get.status_code == 403:
            await ctx.message.channel.send('403 forbidden error')
        
        else:
            await ctx.send("An Error Occured")

    @commands.command()
    async def thank(self, ctx, *, user: discord.Member = None):

        if user == None:
            return await ctx.send("Who do you wanna thank?")

        if user == ctx.author:
            return await ctx.send("You cant thank yourself.")

        else:
            msg = f"{ctx.author.mention} thanked {user.mention}!"
            
        query = "thank"

        search = f"https://api.tenor.com/v1/random?q={query}&key={key}&limit=1&media_filter=basic"
        get = requests.get(search)
        
        if get.status_code == 200:
            json_search = get.json()
            json_check = json_search['next']

            if json_check == "0":
                await ctx.message.channel.send("I didn't found any gifs")

            else:
                try:
                    json_s = json_search['results']
                    
                    image = json_s[0]
                    image = image.get("media")
                    image = image[0]
                    image = image.get("gif")
                    image = image.get("url")


                    embed = discord.Embed(description = msg, color = bot_stuff['none'])

                    embed.set_image(url = image)
                    embed.set_footer(text = f"Source: Tenor")

                    await ctx.message.channel.send(embed=embed)

                except:
                    await ctx.send("Search Term was not valid.")
        
        elif get.status_code == 404:
            await ctx.message.channel.send("404 error")
        
        elif get.status_code == 403:
            await ctx.message.channel.send('403 forbidden error')
        
        else:
            await ctx.send("An Error Occured")

    @commands.command(aliases = ["vibe"])
    async def vibing(self, ctx, *, user: discord.Member = None):

        if user == None:
            return await ctx.send("Who do you wanna vibe with?")

        if user == ctx.author:
            msg = f"{ctx.author.mention} is vibing all alone."
            query = "vibing alone"

        else:
            msg = f"{ctx.author.mention} is vibing with {user.mention}!"
            query = "vibing"

        search = f"https://api.tenor.com/v1/random?q={query}&key={key}&limit=1&media_filter=basic"
        get = requests.get(search)
        
        if get.status_code == 200:
            json_search = get.json()
            json_check = json_search['next']

            if json_check == "0":
                await ctx.message.channel.send("I didn't found any gifs")

            else:
                try:
                    json_s = json_search['results']
                    
                    image = json_s[0]
                    image = image.get("media")
                    image = image[0]
                    image = image.get("gif")
                    image = image.get("url")


                    embed = discord.Embed(description = msg, color = bot_stuff['none'])

                    embed.set_image(url = image)
                    embed.set_footer(text = f"Source: Tenor")

                    await ctx.message.channel.send(embed=embed)

                except:
                    await ctx.send("Search Term was not valid.")
        
        elif get.status_code == 404:
            await ctx.message.channel.send("404 error")
        
        elif get.status_code == 403:
            await ctx.message.channel.send('403 forbidden error')
        
        else:
            await ctx.send("An Error Occured")

    @commands.command()
    async def dance(self, ctx):

        list_of_dances = ['fornite dance', 'call of duty dance', 'anime dance']

        msg = f"{ctx.author.mention} is dancing!"

        query = random.choice(list_of_dances)

        search = f"https://api.tenor.com/v1/random?q={query}&key={key}&limit=1&media_filter=basic"
        get = requests.get(search)
        
        if get.status_code == 200:
            json_search = get.json()
            json_check = json_search['next']

            if json_check == "0":
                await ctx.message.channel.send("I didn't found any gifs")

            else:
                try:
                    json_s = json_search['results']
                    
                    image = json_s[0]
                    image = image.get("media")
                    image = image[0]
                    image = image.get("gif")
                    image = image.get("url")


                    embed = discord.Embed(description = msg, color = bot_stuff['none'])

                    embed.set_image(url = image)
                    embed.set_footer(text = f"Source: Tenor")

                    await ctx.message.channel.send(embed=embed)

                except:
                    await ctx.send("Search Term was not valid.")
        
        elif get.status_code == 404:
            await ctx.message.channel.send("404 error")
        
        elif get.status_code == 403:
            await ctx.message.channel.send('403 forbidden error')
        
        else:
            await ctx.send("An Error Occured")

def setup(bot):
    bot.add_cog(gif_actions(bot))