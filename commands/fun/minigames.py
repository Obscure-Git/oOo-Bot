import discord, random
from discord.ext import commands
from random import randint

class minigames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # choose
    @commands.command(aliases=["choice"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def choose(self, ctx, *, choices: str):
        
        choices = ''.join(choices).split('|')
        await ctx.send(random.choice(choices))


        # 8ball
    @commands.command(aliases=["8ball", "8b"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def _8ball(self, ctx, *, question):
        rndresponse = [
            "Yep!",
            "No..",
            "Positive!",
            "Negative..",
            "Yes!",
            "Nope..",
            "🟢 Green Lights!",
            "🔴 Red Lights.",
            "🟡 Yellow Lights.",
            "50/50"
        ]

        await ctx.send(f"{random.choice(rndresponse)}")


    # toss
    @commands.command(aliases = ["flip"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def toss(self, ctx):
        rndtoss = ["Heads!", "Tails!", "Tie."]

        await ctx.send(f"You got {random.choice(rndtoss)}")


    # rolldice
    @commands.command(aliases=["roll", "rd", "dice", "diceroll"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def rolldice(self, ctx):
        rnddice = ["1", "2", "3", "4", "5", "6"]

        await ctx.send(f"You got a {random.choice(rnddice)}")

    #rock paper scissors
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def rps(self, ctx, *, msg: str):
        
        
        t = ["rock", "paper", "scissors"]

        computer = t[randint(0, 2)]
        player = msg.lower()

        if player == computer:
            await ctx.send(f"{computer}")
            await ctx.send("Tie!")
        
        elif player == "scissors":

            if computer == "rock":
                await ctx.send(f"{computer}")
                await ctx.send("You lose")

            else:
                await ctx.send(f"{computer}")
                await ctx.send("You win!")

        elif player == "rock":
            
            if computer == "paper":
                await ctx.send(f"{computer}")
                await ctx.send(f"You lose")

            else:
                await ctx.send(f"{computer}")
                await ctx.send(f"You win!")

        elif player == "paper":

            if computer == "scissors":
                await ctx.send(f"{computer}")
                await ctx.send("You lose")

            else:
                await ctx.send(f"{computer}")
                await ctx.send("You win!")

        else:
            await ctx.send("Correct options are `rock` , `paper` , `scissors` !")

def setup(bot):
    bot.add_cog(minigames(bot))