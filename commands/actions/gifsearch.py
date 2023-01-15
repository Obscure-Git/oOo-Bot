import discord, json, aiohttp, random, requests, os

from discord.ext import commands

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


class gifsearch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gif(self, ctx, *, query = None):

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


                    embed = discord.Embed(color = bot_stuff['none'])

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
    bot.add_cog(gifsearch(bot))