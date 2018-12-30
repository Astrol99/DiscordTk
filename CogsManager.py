import tkinter as tk
from tkinter import ttk

class mainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Button Style
        style = ttk.Style()
        style.configure("BW.TLabel", font=('tahoma','24', 'bold'), background="white")
        # Main Label
        self.welcomeText = tk.Label(self, text="Cogs Manager", font=('tahoma','24', 'bold'))
        self.welcomeText.pack()
        # Make Command Label
        self.commandLabel = tk.Label(self, text="Command Maker", font=('tahoma', '14'))
        self.commandLabel.pack()
        # Cog Label
        self.cogLabel = tk.Label(self, text="Cog Name:", font=('tahoma', '12'))
        self.cogLabel.pack_propagate(0) 
        self.cogLabel.place(x=125,y=290)
        # Command Cog Name
        self.command_name_ = tk.StringVar()
        self.command_name = tk.Entry(self, textvariable=self.command_name_)
        self.command_name.place(relx=.5, rely=.5, anchor="center")
        # Button Style for makeCommand
        style2 = ttk.Style()
        style2.configure("BA.TLabel", font=('tohoma', '14'), background="Grey", foreground="Light Green")
        # Button to initate new command
        self.makeCommand = ttk.Button(text="Submit", style="BA.TLabel",command=self.openTextBox)
        self.makeCommand.place(x=275,y=320)

    def openTextBox(self, *args, **kwargs):
        # Get string of command name
        self.fileName = None
        self.fileName = str(f"{self.command_name_.get()}.py")
        # Clear entry
        self.command_name.delete(0, 'end')
        # Unpack button and entry
        self.command_name.destroy()
        self.makeCommand.destroy()
        self.cogLabel.destroy()
        # Make new label of name of new cog
        self.cogLabel = tk.Label(self, text=f"Current file Name: {self.fileName}", font=('tohoma', '10'))
        self.cogLabel.place(x=10, y=70)
        # Make text box to edit custom commands
        self.textBox = tk.Text(self, width=80,height=25)
        self.textBox.place(x=10,y=100)
        # Enter template of cogs in text box for setup
        self.textBox.insert(index='1.0',chars='''
import discord
from discord.ext import commands

# IMPORTANT: Make sure to make CLASS NAME different from FILE NAME

# Replace {Cog Name} with your command name
class {Cog Name}}:
    def __init__(self, bot):
        self.bot = bot
    
    # EXAMPLE: command_prefix for now is !
    # Input: "!hello" 
    # Output: "Hello, @User#1337"
    #@commands.command()
    #async def hello(self, ctx):
    #    await ctx.send(f"Hello, {ctx.author.mention}!")
    
# Replace {Cog Name} with the same EXACT name next to class
def setup(bot):
    bot.add_cog({Cog Name}(bot))
        ''')

app = mainApp()
app.title("Cogs Manager")
app.geometry("600x600")
app.mainloop()