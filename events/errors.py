import discord, traceback
from discord.ext import commands

error_color = discord.Color.from_rgb(240, 73, 71)
cross_emoji = "<a:a_cross:778982620347498496>"

class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self , ctx, error):
        
        if hasattr(ctx.command, 'on_error'):
            return


        if isinstance(error, commands.CommandNotFound):
            return


        if isinstance(error, commands.MissingRequiredArgument):
            
            embed = discord.Embed(description = f"{cross_emoji} ***Command used incorrectly. Necessary arguments not provided!***", color= error_color)

            return await ctx.send(embed = embed)


        if isinstance(error, commands.MissingPermissions):
            
            for missing_perm in error.missing_perms:
                permission = missing_perm.replace('_', ' ').replace('guild', 'server').title()

            if len(permission) > 2:
                fmt = '{}, and {}'.format("**, **".join(permission[:-1]), permission[-1])
            else:
                fmt = ' and '.join(permission)

            embed = discord.Embed(description = f"{cross_emoji} ***You dont have permissions to use this command. | `{fmt}`***", color= error_color)

            return await ctx.send(embed = embed)


        if isinstance(error, commands.BotMissingPermissions):
            
            for missing_perm in error.missing_perms:
                permission = missing_perm.replace('_', ' ').replace('guild', 'server').title()

            if len(permission) > 2:
                fmt = '{}, and {}'.format("**, **".join(permission[:-1]), permission[-1])
            else:
                fmt = ' and '.join(permission)

            embed = discord.Embed(description = f"{cross_emoji} ***I dont have enough permissions to execute this command. | `{fmt}`***")


        if isinstance(error, commands.CommandOnCooldown):
            
            msg =  "***The command is on cooldown. Try again in {:.2f}s.***".format(error.retry_after)

            embed = discord.Embed(description = f"{cross_emoji} {msg}", color= error_color)

            return await ctx.send(embed = embed)


        if isinstance(error, commands.DisabledCommand):
            
            embed = discord.Embed(description = f'{cross_emoji} ***That command has been disabled.***', color = error_color)
            
            return await ctx.send(embed = embed)


        if isinstance(error, commands.CheckFailure):
            
            embed = discord.Embed(description = f"{cross_emoji} ***You donot have permissions to use this command.***", color = error_color)
            
            return await ctx.send(embed = embed)


        if isinstance(error, commands.NoPrivateMessage):
            try:
                embed = discord.Embed(description = f"{cross_emoji} ***This command cannot be used in direct messages.***", color = error_color)
                return await ctx.send(embed = embed)
            
            except discord.Forbidden:
                pass
            
            return


        if isinstance(error, commands.UserInputError):
            
            embed = discord.Embed(description = f"{cross_emoji} ***Invalid Input***", color = error_color)
            
            return await ctx.send(embed = embed)


        else:
            tb = '\n'.join(traceback.format_exception(type(error), error, error.__traceback__))

            embed = discord.Embed(description = f"```py\n{tb[:1992]}\n```", color = error_color)

            return await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(errors(bot))