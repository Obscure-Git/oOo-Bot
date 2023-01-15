import discord, pymongo, os

from discord.ext import commands
from pymongo import MongoClient

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["changeprefix", 'prefix'])
    @commands.guild_only()
    @commands.has_permissions(administrator = True)
    async def setprefix(self, ctx, prefix):
        
        mongo_url = os.environ['Mongodb']

        cluster = MongoClient(mongo_url)

        db = cluster['obotdb']

        collection = db['prefixes']

        guild = ctx.message.guild.id

        query = {"_id": guild}

        if (collection.count_documents(query) == 0):

            new_prefix = {"_id": guild, "prefix": prefix}

            collection.insert_one(new_prefix)

            await ctx.channel.send(f"Prefix was changed to `{prefix}`")

        else:
            query = {"_id": guild}

            prefixes = collection.find(query)

            new_prefix = prefix

            collection.update_one({"_id": guild}, {"$set":{"prefix":prefix}})

            await ctx.channel.send(f"Prefix was changed to `{prefix}`")


def setup(bot):
    bot.add_cog(test(bot))