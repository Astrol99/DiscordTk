import discord
from discord.ext import commands

#TODO: Start on kick command and import adminList.txt

class Moderation:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def kick(self, ctx, user=None, reason="No reason"):
        await ctx.send(f"Banned: {user}\nReason: {reason}")
    

def setup(bot):
    bot.add_cog(Moderation(bot))