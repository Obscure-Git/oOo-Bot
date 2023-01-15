import discord, os, traceback, sys, json, asyncio, pymongo

from pymongo import MongoClient
from discord.ext import commands

def get_prefix(bot, message):

    mongo_url = os.environ['Mongodb']

    cluster = MongoClient(mongo_url)

    db = cluster['obotdb']

    collection = db['prefixes']

    if not message.guild:
        return "+"

    try:
        query = {"_id": message.guild.id}

        if (collection.count_documents(query) == 0):
            return "+"

        else:
            data = collection.find(query)

            for result in data:
                data = result["prefix"]

            return data
    
    except:
        return "+"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = (get_prefix), case_insensitive = True, intents = intents)

@bot.remove_command("help")

@bot.command()
async def mainpy(ctx):
    await ctx.send("Ok")


print(
    """
-----------------------------------------------
------------------COMMANDS---------------------
-----------------------------------------------
    """
)

for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"commands.{filename[:-3]}")
            print(f"{filename} commands load successful.")

        except Exception as e:
            print(f"Failed to load {filename} commands", file=sys.stderr)
            traceback.print_exc()

for filename in os.listdir("./commands/actions"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"commands.actions.{filename[:-3]}")
            print(f"{filename} commands load successful.")

        except Exception as e:
            print(f"Failed to load {filename} commands", file=sys.stderr)
            traceback.print_exc()

for filename in os.listdir("./commands/fun"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"commands.fun.{filename[:-3]}")
            print(f"{filename} commands load successful.")

        except Exception as e:
            print(f"Failed to load {filename} commands", file=sys.stderr)
            traceback.print_exc()

print(
    """
-----------------------------------------------
--------------------EVENTS---------------------
-----------------------------------------------
    """
)
for filename in os.listdir("./events"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"events.{filename[:-3]}")
            print(f"{filename} events load successful.")

        except Exception as e:
            print(f"Failed to load {filename} events", file=sys.stderr)
            traceback.print_exc()

bot.run(os.environ['Token'])