from tkinter import *
from tkinter import ttk
#import controller
import time
import os
import sys
import asyncio

try:
    import discord
    from discord.ext import commands
except Exception as importError:
    print("Error importing discord, did you install discord.py?")
    print("If not, type 'pip3 install discord.py' ")
    print("Exiting...")
    sys.exit()

# TODO: Make an output widget

root = Tk()
root.geometry("400x200")
root.title("Discord Bot Generator")

# Make tk window not resizable
root.resizable(False, False)

# Style for all tk windows

root.configure(background="#36393f")

# Style ===============================================================

buttonStyle = ttk.Style()
buttonStyle.configure("BW.TButton", foreground="Light Green", background="#36393f")

# Initalizing widgets =========================================================================================

welcomeLabel = Label(root, text="Discord Bot Generator", font=("helvetica", 20), background="#36393f", foreground="white")
stepLabel = Label(root, text="Please enter your bot token and command prefix", font=("helvetica", 8), background="#36393f", foreground="white")

welcomeLabel.pack(side=TOP)
stepLabel.pack(side=TOP)

token_ = StringVar()
prefix_ = StringVar()

tokenEntry = Entry(root, textvariable=token_, background="#36393f", foreground="white")
prefixEntry = Entry(root, textvariable=prefix_, background="#36393f", foreground="white")

labelWarn = Label(root, text="Exiting...", fg="red", font=("helvetica", 9))

#Output Widget - Under Construction

#output_ = StringVar()
#outputEntry = Entry(root, textvariable=output_)

# Starts Bot =========================================================================================

def initiateBot(token_read=False):

    global root
    global labelWarn

    labelWarn.pack(side=TOP)

    prefix = str(prefix_.get())
    prefixEntry.delete(0, 'end')

    token = str(token_.get())
    tokenEntry.delete(0, 'end')

    # Destroys current tkinter window
    root.destroy()

    #Reads token.txt for token and prefix info
    if token_read == True:
        with open("token.txt") as f:
            mylist = f.read().splitlines()
            token = mylist[0]
            prefix = mylist[1]
            f.close()
            
        print("\n=====Loading token.txt...=====\n")
        print("Done!")


    # Then shows output on command
    print("\n=====STARTUP DETAILS=====")
    print("\nRunning on the discord version of: {}".format(discord.__version__))
    print("Prefix: {}".format(prefix))
    print("Token: {}".format(token))

    main_extensions = [
        #"controller",
        "cogs.Main_Functions",
        "cogs.fun",
        "cogs.mod"
    ]

    with open("adminList.txt") as fi:
        admin_list = fi.read().splitlines()
        fi.close()


    bot = commands.Bot(command_prefix=prefix, status=discord.Status.idle, activity=discord.Game(name="Booting..."))

    @bot.event
    async def on_ready():
        print("\n=====BOT STATUS=====")
        print("Current Status: Online!")
        print("Logged in as '{}#{}'".format(bot.user.name, bot.user.id))
        print("Bot id: {}".format(bot.user.id))
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Online"))
        print("\n=====BOT STATISTICS=====\n")
        print(f"Server Count: {len(bot.guilds)}\n")
        print(f"User Count: {len(bot.users)}")

    @bot.command()
    async def shutdown(ctx):
        currentID = (f"{ctx.author.id}")

        if currentID in admin_list:
            await ctx.channel.send("Going offline...")
            time.sleep(3)
            await ctx.channel.send("Goodbye...")
            sys.exit(f"User: {ctx.author.name} UserID: {ctx.author.id} executed the command 'shutdown' ")

        elif currentID not in admin_list:
            await ctx.channel.send("Unauthorized user!")

    @bot.command()
    async def list(ctx):
        final = "List of extensions:\n"

        for ext in main_extensions:
            sep = "{}\n".format(ext)
            final += sep

        await ctx.channel.send("```css\n{}\n```".format(final))

    @bot.command()
    async def load(ctx, extension_name : str):
        #Loads main_extensions

        try:
            bot.load_extension(extension_name)
        except Exception as e:
            await ctx.channel.send("Failed to import extensions | :cry:\nError:\n```py\n{}\n```".format(str(e)))
            return

        await ctx.channel.send("Loaded {} | :open_mouth:".format(extension_name))

    @bot.command()
    async def unload(ctx, extension_name : str):
        try:
            bot.unload_extension(extension_name)
            await ctx.channel.send("Unloaded {}".format(extension_name))
        except Exception as e:
            await ctx.channel.send("Couldn't unload {}\n```py\n{}\n```".format(extension_name, e))

    @bot.command()
    async def reload(ctx, extension_name: str):
        try:
            bot.unload_extension(extension_name)
            bot.load_extension(extension_name)
            await ctx.send(f"Reloaded extension: {extension_name}")
        except Exception as e:
            await ctx.send(f"Couldn't reload {extension_name}\n```py\n{e}\n```")

    @bot.command()
    async def idMe(ctx):
        await ctx.send(f"{ctx.author.mention} your user id is: {ctx.author.id}")
    
    @bot.command()
    async def addAdmin(ctx, userId: str=None):
        currentId = (f"{ctx.author.id}")

        if currentId in admin_list:
            if userId == None or len(userId) != 18:
                await ctx.send("Invalid user id!")
            else:
                await ctx.send(f"Added {userId} to admin list!")
                file = open("adminList.txt", "a+")
                file.write(f"{userId}\n")
                file.close()
        else:
            await ctx.send("You dont have perms to do that!")

    @bot.command()
    async def removeAdmin(ctx, userId: str=None):
        currentId = (f"{ctx.author.id}")

        if currentId in admin_list:
            if userId == None or len(userId) != 18:
                await ctx.send("Invalid user id!")
            else:
                await ctx.send(f"Removed {userId} from admin list!")
                file = open("adminList.txt", "r")
                lines = file.readlines()
                file.close()
                file = open("adminList.txt", "w")
                for line in lines:
                    if line != f"{userId}"+"\n":
                        file.write(line)
                file.close
        else:
            await ctx.send("You dont have perms to do that!")
    
    @bot.command()
    async def adminList(ctx):
        await ctx.send("Current admin list:")
        file = open("adminList.txt", "r")
        for line in file:
            await ctx.send(f"{line}")

    if __name__ == '__main__':
        print("\n=====LOADING EXT=====")
        print("\nLoading Extensions...")

        time.sleep(3)

        for extension in main_extensions:
            try:
                bot.load_extension(extension)
                print("Loaded {} successfully!".format(extension))
            except Exception as e:
                print("\nFATAL ERROR:\nFailed to load extension: {}".format(extension))
                print("Error Message: {}\n".format(e))

    bot.run(token)

# Packing widgets =========================================================================================

startButton = ttk.Button(root, text="Enter", style="BW.TButton", command=initiateBot)
startToken = ttk.Button(root, text="Load Token.txt", style="BW.TButton", command=lambda: initiateBot(token_read=True))

tokenLabel = Label(root, text="Token: ", background="#36393f", foreground="white")
prefixLabel = Label(root, text="Prefix: ", background="#36393f", foreground="white")

tokenLabel.place(x=0,y=100)
tokenEntry.place(x=53,y=100)

prefixLabel.place(x=0, y=125)
prefixEntry.place(x=53, y=130)

startButton.place(x=305, y=100)
startToken.place(x=270, y=130)

root.mainloop()