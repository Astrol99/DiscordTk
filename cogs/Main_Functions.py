import discord
from discord.ext import commands

class main_functions:
    def __init__(self, bot):
        self.bot = bot

    admin_list = [
        "354693078495264778"
    ]

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(":ping_pong: | Pong! {} ms".format(self.bot.latency*1000))

    #@commands.command()
    #async def ban(ctx,self, member: discord.Member, reason: str):
    #    global admin_list
    #
    #    if self.author.id not in admin_list:
    #        await self.send("Unauthorized user!")
    #    elif user == self.author.mention:
    #        await self.send("You can't ban yourself!")
#
#        if reason == None:
#            reason = "No reason"

#        await self.ban(user)
    @commands.command()
    async def repeat(self, ctx, *, message: str):
        await self.send(message)

def setup(bot):
    bot.add_cog(main_functions(bot))
