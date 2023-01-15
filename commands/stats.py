import discord, platform, psutil, os, decimal
from discord.ext import commands
from datetime import datetime

bot_stuff = {
    "success": discord.Color.from_rgb(67, 180, 129),
    "fail": discord.Color.from_rgb(240, 73, 71),
    "none": discord.Color.from_rgb(47, 49, 54),
    "support": "https://discord.gg/s2khsve",
    "botinv": "https://discord.com/oauth2/authorize?client_id=772818044933242880&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2Finvite%2Fs2khsve&scope=bot",
    "website": "https://obot.netlify.app/",
    "owner": "Obscure#4857"
}

launch_time = datetime.utcnow()

class stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['latency', 'lat'])
    async def ping(self, ctx):
        await ctx.send(f"`{round(self.bot.latency * 1000)}ms`")

    @commands.command()
    async def stats(self, ctx):

        guilds = len(self.bot.guilds)
        ping = f"{round(self.bot.latency * 1000)} ms"
        
        system = platform.system()

        delta_uptime = datetime.utcnow() - launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        ram_usage_percentage = f"{psutil.virtual_memory().percent} %"
        cpu_percent = f"{psutil.cpu_percent()} %"
        cpu_count = psutil.cpu_count()

        available_ram_percent = f"{round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)} %"

        total_ram = round((psutil.virtual_memory().total /1024/1024))
        used_ram = round(psutil.virtual_memory().used /1024/1024)
        free_ram = round(psutil.virtual_memory().free /1024/ 1024)
        frgb = "mb"
        urgb = "mb"
        trgb = "mb"

        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        memberCount = len(self.bot.users)

        if free_ram > 1024:
            free_ram = f"{float('%.2f'%(free_ram / 1024))}"
            frgb = "gb"

        if used_ram > 1024:
            used_ram = f"{float('%.2f'%(used_ram / 1024))}"
            urgb = "gb"

        if total_ram > 1024:
            total_ram = f"{float('%.2f'%(total_ram / 1024))}"
            trgb = "gb"

        embed = discord.Embed(color = bot_stuff["success"])
        
        embed.add_field(name = "Bot", value = f"```asciidoc\nName:: oOo#7488 (772818044933242880)\nOwner:: {bot_stuff['owner']}\nPython Version:: {pythonVersion}\nDiscord Version:: {dpyVersion}```", inline=False)
        
        embed.add_field(name = "Stats", value = f"```asciidoc\nGuilds:: {guilds}\nUsers:: {memberCount}\nPing:: {ping}\nUptime:: {days}d {hours}h {minutes}m```")
        
        embed.add_field(name = "System", value = f"```asciidoc\nOS:: {system}\nCPU Usage:: {cpu_percent}\nCPU Cores:: {cpu_count}```", inline=False)
        
        embed.add_field(name = "RAM", value = f"```asciidoc\nTotal RAM:: {total_ram} {trgb}\nRAM Usage:: {used_ram} {urgb} ({ram_usage_percentage})\nAvailable RAM:: {free_ram} {frgb} ({available_ram_percent})```", inline=False)

        embed.add_field(name = "Links", value = f"[Support Server]({bot_stuff['support']}) | [Invite]({bot_stuff['botinv']}) | [Website and Documentation]({bot_stuff['website']})", inline=False)

        embed.set_thumbnail(url = self.bot.user.avatar_url)

        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(stats(bot))