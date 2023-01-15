import discord, os
from discord.ext import commands
import asyncio
import json

import pymongo
from pymongo import MongoClient

class onMessage(commands.Cog, name="onMessage"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):

        mongo_url = os.environ['Mongodb']

        cluster = MongoClient(mongo_url)

        db = cluster['obotdb']

        collection = db['prefixes']

        if not msg.guild:
            prefix = "+"
            

        try:
            query = {"_id": msg.guild.id}

            if (collection.count_documents(query) == 0):
                prefix = "+"

            else:
                data = collection.find(query)

                for result in data:
                    data = result["prefix"]

                prefix = data


        except:
            prefix = "+"


        if self.bot.user.mentioned_in(msg):
            await msg.channel.send(f"My prefix here is `{prefix}`.")


def setup(bot):
    bot.add_cog(onMessage(bot))
