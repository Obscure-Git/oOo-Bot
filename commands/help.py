import discord
from discord.ext import commands

class help_msg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["commands", "cmds", "help"])
    async def _help(self, ctx):

        e = discord.Embed(description= "Prefix: `+`", color = discord.Color.from_rgb(47, 49, 54))

        e.add_field(name = "Help & Support", value = "• [Commands List](https://obot.gitbook.io/docs/)\n• [oOo Website](https://obot.netlify.app/)", inline=False)

        e.add_field(name = "oOo", value = "• [Invite oOo](https://discord.com/oauth2/authorize?client_id=772818044933242880&permissions=1611005025&scope=bot)\n• [Support Server](https://discord.gg/s2khsve/)")
        
        e.set_footer(text = f"Built by Obscure#6969", icon_url="https://cdn.discordapp.com/avatars/755436063828213821/a_eb5c0ff201ede83183846f61036f4173.gif?size=1024")

        e.set_author(name = f"{ctx.message.guild.name}", icon_url= ctx.message.guild.icon_url)

        emoji = "<a:verify:769900861584834571>" #Your bot must be a part of our server to be able to use this emoji

        await ctx.message.add_reaction(emoji)

        await ctx.author.send(embed = e)

def setup(bot):
    bot.add_cog(help_msg(bot))