import discord, requests, json, random
from discord.ext import commands

no_color = discord.Color.from_rgb(47, 49, 54)

class pics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases = ['pics', 'pic'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def photography(self, ctx):

        r = requests.get("https://memes.blademaker.tv/api/EarthPorn?lang=en")

        res = r.json()

        title = res['title']
        upvotes = res['ups']
        nsfw = res['nsfw']
        image = res['image']
        author = res['author']
        post_id = res['id']

        post_link = f"https://www.reddit.com/r/EarthPorn/comments/{post_id}"

        while nsfw == False:
            try:
                embed = discord.Embed(description = f"**[{title}]({post_link})**", color = no_color)

                embed.set_image(url = image)

                embed.set_footer(text = f"⬆️ Upvotes: {upvotes} | Author: {author}")

                sent = await ctx.send(embed = embed)

                await sent.add_reaction('⬆️')
                await sent.add_reaction('⬇️')
                break
            
            except:
                await ctx.send("An API error occured!")
                break



    @commands.command(aliases = ['foods'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def food(self, ctx):

        r = requests.get("https://memes.blademaker.tv/api/Food?lang=en")

        res = r.json()

        title = res['title']
        upvotes = res['ups']
        nsfw = res['nsfw']
        image = res['image']
        author = res['author']
        post_id = res['id']

        post_link = f"https://www.reddit.com/r/Food/comments/{post_id}"

        while nsfw == False:
            try:
                embed = discord.Embed(description = f"**[{title}]({post_link})**", color = no_color)

                embed.set_image(url = image)

                embed.set_footer(text = f"⬆️ Upvotes: {upvotes} | Author: {author}")

                sent = await ctx.send(embed = embed)

                await sent.add_reaction('⬆️')
                await sent.add_reaction('⬇️')
                break
            
            except:
                await ctx.send("An API error occured!")
                break

def setup(bot):
    bot.add_cog(pics(bot))