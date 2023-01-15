import discord
from discord.ext import commands

import asyncio
import time

no_color = discord.Color.from_rgb(47, 49, 54)

class Polls(commands.Cog, name="Polls"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['polls'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def poll(self, ctx):

        if ctx.channel.permissions_for(ctx.guild.me).embed_links:
            embed = discord.Embed(title="Polls", color = discord.Color.from_rgb(67, 180, 129) )

            embed.add_field(
                            name = "Available Poll Types:" , 
                            value = " • [Quick Polls](https://obot.gitbook.io/docs/commands/polls#quick-polls) \n • [Advanced Polls](https://obot.gitbook.io/docs/commands/polls#advanced-polls) \n • [Would You Rather Poll](https://obot.gitbook.io/docs/commands/polls#would-you-rather-polls)")

            await ctx.send(embed = embed)

        else:
            await ctx.send("go to this website for help regarding polls --> https://obot.gitbook.io/docs/commands/polls")




    @commands.command(aliases = ["wyrpoll", "wouldyourather", "wpoll"])
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def wyr(self, ctx, emoji1 , option1, emoji2, option2):
        
        embed = discord.Embed(title = "Would you rather", description = f"\n{emoji1} {option1}\n{emoji2} {option2}", color = discord.Color.from_rgb(67, 180, 129))

        react_message = await ctx.send(embed = embed)

        reactions = [emoji1 , emoji2]

        for reaction in reactions:
            await react_message.add_reaction(reaction)
        


    @commands.command(aliases = ['apoll'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def advpoll(self, ctx, question, emojis, *, options: str):

        options = ''.join(options).split('|')
        emojis = ''.join(emojis).split('/')

        reactions = emojis

        if len(emojis) != len(options):

            errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> Number of emojis and options didn't match! Make sure that there are no spaces before or after any emojis or the `/` sign***")

            await ctx.send(embed = errorembed)
            return

        if len(options) <= 1:

            errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> You need more than 1 option to make a poll!***")

            await ctx.send(embed = errorembed)
            return
        
        if len(options) > 5:

            errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> You cannot make a custom emoji poll with more than 5 options!***")

            await ctx.send(embed = errorembed)
            return

        if " " in reactions:
            errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> Please make sure that there are no spaces before or after emojis!***")
            await ctx.send(embed = errorembed)
            return
        
        description = []

        for x, option in enumerate(options):

            try:
                description += '\n {} {}\n'.format(reactions[x], option)

            except:
                if reactions[x] != discord.Emoji:
                    errorembed.set_description(f"***<a:a_cross:778982620347498496> Invalid emoji used! {reactions[x]}***")
                    await ctx.send(embed = errorembed)
                
                else:
                    errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> An Unknown Error occured!***")



        if ctx.channel.permissions_for(ctx.guild.me).embed_links:
            pollembed = discord.Embed(title=question, description=''.join(description), color = discord.Color.from_rgb(67, 180, 129) )

        else:
            msg = "***<a:a_cross:778982620347498496> I donot have embed links permissions!***"
            await ctx.send(msg)
            return

        react_message = await ctx.send(embed= pollembed)

        for reaction in reactions[:len(options)]:

            if ctx.channel.permissions_for(ctx.guild.me).add_reactions:
                try:
                    await react_message.add_reaction(reaction)

                except:
                    if ctx.channel.permissions_for(ctx.guild.me).use_external_emojis:
                        await react_message.delete()

                        errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> An unknown error occured! Make sure the emojis belong to a server I m in!***")
                        await ctx.send(embed = errorembed)
                        return

                    else:
                        await react_message.delete()

                        errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> I donot have permissions to use external emojis!***")
                        await ctx.send(embed = errorembed)
                        return
                
                

            else:
                await react_message.delete()
                errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> I donot have permissions to add reactions!***", delete_after = 5)
                await ctx.send(embed = errorembed)
                return



    @commands.command(aliases = ['qpoll'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def quickpoll(self, ctx, question, *, options: str):

        options = ''.join(options).split('|')

        reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']

        if len(options) <= 1:

            errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> You need more than 1 option to make a poll!***")

            await ctx.send(embed = errorembed)
            return
        
        if len(options) > 5:

            errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> You cannot make a custom emoji poll with more than 5 options!***")

            await ctx.send(embed = errorembed)
            return

        description = []

        for x, option in enumerate(options):

            try:
                description += '\n {} {}\n'.format(reactions[x], option)

            except:
                errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> An Unknown Error occured!***")
                await ctx.send(embed = errorembed)
                return

        if ctx.channel.permissions_for(ctx.guild.me).embed_links:
            pollembed = discord.Embed(title=question, description=''.join(description), color = discord.Color.from_rgb(67, 180, 129) )

        else:
            await ctx.send(f"I donot have embed links permissions!")
            return

        react_message = await ctx.send(embed= pollembed)

        for reaction in reactions[:len(options)]:

            if ctx.channel.permissions_for(ctx.guild.me).add_reactions:
                try:
                    await react_message.add_reaction(reaction)

                except:
                    await react_message.delete()
                    
                    errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> An unknown error occured!***")
                    await ctx.send(embed = errorembed)
                    return
            
                

            else:
                await react_message.delete()
                errorembed = discord.Embed(color = discord.Color.from_rgb(240, 73, 71) ,description = "***<a:a_cross:778982620347498496> I donot have permissions to add reactions!***", delete_after = 5)
                await ctx.send(embed = errorembed)
                return

def setup(bot):
    bot.add_cog(Polls(bot))
