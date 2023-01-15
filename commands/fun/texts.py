import discord, random, asyncio, re
from discord.ext import commands

from PIL import Image


class texts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['backwards', 'bw'])
    async def reverse(self, ctx, *, msg:str):
        await ctx.send(msg[::-1])

    @commands.command(aliases = ['upper', 'uc'])
    async def uppercase(self, ctx, *, msg:str):
        await ctx.send(msg.upper())

    @commands.command(aliases = ['lower', 'lc'])
    async def lowercase(self, ctx, *, msg:str):
        await ctx.send(msg.lower())

    # emojify
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def emojify(self, ctx, *, text: str):
        emojified = "\n"
        formatted = re.sub(r"[^A-Za-z ]+", "", text).lower()
        if text == "":
            await ctx.send("Remember to say what you want to convert!")

        else:
            for i in formatted:
                if i == " ":
                    emojified += "     "
                else:
                    emojified += ":regional_indicator_{}: ".format(i)

            if len(emojified) + 2 >= 2000:
                await ctx.send("Your message in emojis exceeds 2000 characters!")
            if len(emojified) <= 25:
                await ctx.send("Your message could not be converted!")
            else:
                await ctx.send(emojified)



    # spoilify
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def spoilify(self, ctx, *, text: str):
        
        spoilified = " \n"
        
        if text == "":
            await ctx.send("Remember to say what you want to convert!")
        
        else:
            
            for i in text:
                spoilified += "||{}||".format(i)
            
            if len(spoilified) + 2 >= 2000:
                await ctx.send("Your message in spoilers exceeds 2000 characters!")

            if len(spoilified) <= 4:
                await ctx.send("Your message could not be converted!")
            
            else:
                await ctx.send(spoilified)


            
    # color
    @commands.command(aliases = ['colour'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def color(self, ctx, *, inputcolor=""):

        if inputcolor == "":
            
            randgb = lambda: random.randint(0, 255)
            
            hexcode = "%02X%02X%02X" % (randgb(), randgb(), randgb())
            
            rgbcode = str(tuple(int(hexcode[i : i + 2], 16) for i in (0, 2, 4)))
            
            await ctx.send("`Hex: #" + hexcode + "`\n`RGB: " + rgbcode + "`")
            
            heximg = Image.new("RGB", (64, 64), "#" + hexcode)
            heximg.save("color.png")

            await ctx.send(file=discord.File("color.png"))
        
        else:
        
            if inputcolor.startswith("#"):
                hexcode = inputcolor[1:]

                if len(hexcode) == 8:
                    hexcode = hexcode[:-2]

                elif len(hexcode) != 6:
                    await ctx.send("Make sure hex code is this format: `#7289DA`")
                
                rgbcode = str(tuple(int(hexcode[i : i + 2], 16) for i in (0, 2, 4)))
                
                await ctx.send("`Hex: #" + hexcode + "`\n`RGB: " + rgbcode + "`")
                
                heximg = Image.new("RGB", (64, 64), "#" + hexcode)
                
                heximg.save("color.png")
                
                await ctx.send(file=discord.File("color.png"))
            
            else:
                await ctx.send("Make sure hex code is this format: `#7289DA`")




def setup(bot):
    bot.add_cog(texts(bot))
