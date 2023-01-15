import discord, json, random, requests, aiohttp

from discord.ext import commands
from aiohttp import request
from random import randint

api_creds = "Source: Nekobot API"
tweet_color = discord.Color.from_rgb(76, 154, 229) 
no_color = discord.Color.from_rgb(47, 49, 54)

class memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['memes', 'dankmemes'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self, ctx):

        subreddits = ['memes', 'wholesomememes', 'dankmemes', 'meme']

        random_sr = random.choice(subreddits) 

        r = requests.get(f"https://memes.blademaker.tv/api/{random_sr}?lang=en")

        res = r.json()

        title = res['title']
        upvotes = res['ups']
        nsfw = res['nsfw']
        image = res['image']
        author = res['author']
        post_id = res['id']

        post_link = f"https://www.reddit.com/r/{random_sr}/comments/{post_id}"

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

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meirl(self, ctx):

        r = requests.get("https://memes.blademaker.tv/api/meirl?lang=en")

        res = r.json()

        title = res['title']
        upvotes = res['ups']
        nsfw = res['nsfw']
        image = res['image']
        author = res['author']
        post_id = res['id']

        post_link = f"https://www.reddit.com/r/meirl/comments/{post_id}"

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

    @commands.command(aliases = ['funnyposts'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def funny(self, ctx):

        r = requests.get("https://memes.blademaker.tv/api/Funny?lang=en")

        res = r.json()

        title = res['title']
        upvotes = res['ups']
        nsfw = res['nsfw']
        image = res['image']
        author = res['author']
        post_id = res['id']

        post_link = f"https://www.reddit.com/r/Funny/comments/{post_id}"

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


    @commands.command(aliases = ['sts', 'randomthoughts', 'rts'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def showerthoughts(self, ctx):

        subreddit = 'Showerthoughts' #subreddit that will be used \\ syntax can differ for each subreddits 
        count = 1 #number of posts to get at a time \\ slower when more
        timeframe = 'all' #day night all
        listing = 'random' #hot new top // this also changes the syntax of #get-data
        
        def get_reddit(subreddit,count):

            base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?count={count}&t={timeframe}'
            request = requests.get(base_url, headers = {'User-agent': 'yourbot'})

            return request.json()
        
        top_post = get_reddit(subreddit,count)

        #get-data
        title = top_post[0]['data']['children'][0]['data']['title']
        url = top_post[0]['data']['children'][0]['data']['url']
        author = top_post[0]['data']['children'][0]['data']['author']
        nsfw = top_post[0]['data']['children'][0]['data']['over_18'] 
        ups = top_post[0]['data']['children'][0]['data']['ups'] 

        while nsfw == False:
            try:
                embed = discord.Embed(description = f"**[{title}]({url})**", color = no_color)

                embed.set_footer(text = f"⬆️ Upvotes: {ups} | Author: {author}")

                sent = await ctx.send(embed = embed)

                await sent.add_reaction('⬆️')
                await sent.add_reaction('⬇️')
                break
            
            except:
                await ctx.send("An API error occured!")
                break

    @commands.command(aliases = ['uo'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unpopularopinion(self, ctx):

        subreddit = 'unpopularopinion' #subreddit that will be used \\ syntax can differ for each subreddits 
        count = 1 #number of posts to get at a time \\ slower when more
        timeframe = 'all' #day night all
        listing = 'random' #hot new top // this also changes the syntax of #get-data
        
        def get_reddit(subreddit,count):

            base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?count={count}&t={timeframe}'
            request = requests.get(base_url, headers = {'User-agent': 'yourbot'})

            return request.json()
        
        top_post = get_reddit(subreddit,count)

        #get-data
        title = str(top_post[0]['data']['children'][0]['data']['title'])
        url = str(top_post[0]['data']['children'][0]['data']['url'])
        author = str(top_post[0]['data']['children'][0]['data']['author'])

        nsfw = top_post[0]['data']['children'][0]['data']['over_18'] 
        
        ups = str(top_post[0]['data']['children'][0]['data']['ups']) 
        desc = str(top_post[0]['data']['children'][0]['data']['selftext'])

        text = len(desc) + len(url)

        while text < 2030:
            while nsfw == False:
                try:
                    embed = discord.Embed(title = f"{title}", description = f"{desc}\n[Original Post]({url})", color = no_color)

                    embed.set_footer(text = f"⬆️ Upvotes: {ups} | Author: {author}")

                    sent = await ctx.send(embed = embed)

                    await sent.add_reaction('⬆️')
                    await sent.add_reaction('⬇️')
                    break

                except:
                    await ctx.send("An API error occured!")
                    break
            break            

def setup(bot):
    bot.add_cog(memes(bot))