import discord
from discord.ext import commands
import random

class Fun:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def urmum(self, ctx):
        insults = [
            "gay",
            "lesbian",
            "fat",
            "skinny",
            "dumb",
            "old",
            "stupid"
        ]

        await ctx.send(f"{ctx.author.mention}, Ur mum {random.choice(insults)}")
    
    @commands.command()
    async def roll(self, ctx):
        num = random.randint(0, 100)
        response = None

        if num >= 50:
            response = "Yep!"
        else:
            response = "Nope"

        text = f"{ctx.author.mention} rolled {num}\nAnswer: {response}"
        
        embed = discord.Embed(
            title = "Roll Game",
            description = text,
            color = discord.Colour.blue()
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/527665456727982082/528286468314103815/dice-png-transparent-images--png-all-4.png")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))