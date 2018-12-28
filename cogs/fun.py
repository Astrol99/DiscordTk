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

        await ctx.send(f"{ctx.author.mention} rolled {num}\nAnswer: {response}")

def setup(bot):
    bot.add_cog(Fun(bot))