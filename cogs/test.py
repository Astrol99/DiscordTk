import discord
from discord.ext import commands

class Test:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        # Self is not a good way to send a discord bot message
        await ctx.send("Hey there!")

def setup(bot):
    bot.add_cog(Test(bot))
