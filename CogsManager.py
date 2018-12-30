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
        #style2 = ttk.Style()
        #style2.configure("BA.TLabel", font=('tohoma', '14'), background="Grey", foreground="Light Green")
        # Button to initate new command
        self.makeCommand = tk.Button(text="Submit", command=self.openTextBox, font="tohoma 14", fg="light green")
        self.makeCommand.place(x=275,y=320)
    
    def error_window(self, textError="Unknown"):
        rootMIN = tk.Tk()
        rootMIN.title("ERROR")
        rootMIN.geometry("400x200")
        errorLabel = tk.Label(rootMIN, text=f"ERROR: {textError}")
        errorLabel.place(relx=.5, rely=.5, anchor="center")
        def closeWin():
            rootMIN.destroy()
        okButtonMIN = tk.Button(rootMIN, text="Ok",command=closeWin)
        okButtonMIN.place(x=180,y=170)
        rootMIN.mainloop()

    def openTextBox(self, *args, **kwargs):
        # Get string of command name
        self.fileName = None
        self.fileName = str(f"{self.command_name_.get()}.py".replace(" ", ""))
        # Gets list of cogs
        with open("cog_list.txt") as se:
            cog_list = se.read().splitlines()
            se.close()
        # Checks if cog name is empty
        if len(self.command_name.get()) == 0 or self.command_name.index("end") == 0 or self.fileName in cog_list or " " in self.fileName:
            self.error_window(textError="Cog already exists or name is empty!")
            return
        # Finally destroy all main widgets
        self.command_name.delete(0, 'end')
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
        # Make save button
        self.cogSave = tk.Button(self, text="Save", command=self.saveCog)
        self.cogSave.place(x=540,y=50)

    # Pop-up window when finished with everything
    def doneWindow(self):
        doneRoot = tk.Tk()
        # Frame Setup
        doneRoot.title("Finished")
        doneRoot.geometry("600x200")

        # Main Labels
        finishH1 = tk.Label(doneRoot, text="FINISHED", font="Tohoma 18 bold")
        finishH1.pack()
        finishedLabel = tk.Label(doneRoot, text="Finished applying new cog!")
        finishedLabel.pack()
        cogDir = tk.Label(doneRoot, text=f"Cogs dir is saved at: {self.currentFilePath}/cogs")
        cogDir.pack()
        extDir = tk.Label(doneRoot, text=f"{self.fileName} is saved at: {self.currentFilePath}/cogs/{self.fileName}")
        extDir.pack()

        # Destroy all
        def destroyAll():
            doneRoot.destroy()
            app.destroy()

        # Finish Button
        finishBut = tk.Button(doneRoot, text="Finish", command=destroyAll)
        finishBut.pack()

        doneRoot.mainloop()

    # Command to save cog
    def saveCog(self):
        # Import OS here since this is the only place required
        import os
        # Used to detect OS
        import platform
        # Get all of text in text box
        pure_input = self.textBox.get("1.0", tk.END)
        # Current absolute dir
        self.currentFilePath = os.path.dirname(os.path.abspath("CogsManager.py"))
        # Checks if is windows or not
        if platform.system() == "Windows":
            start = "C:/"
        else:
            start = ""
        # Bool if path exists
        try:
            checkDir = os.path.isdir(f"{start}{self.currentFilePath}/cogs/")
        except:
            try:
                start = "D:/"
                checkDir = os.path.isdir(f"{start}{self.currentFilePath}/cogs/")
            except Exception as e:
                self.error_window(textError=f"Something went wrong when checking cogs dir!\n{e}")
                return
        # If it doesn't, make a dir called cogs
        if checkDir == False:
            # Using try if something is wrong based on OS
            try:
                os.makedirs(f"{start}{self.currentFilePath}/cogs/")
            except Exception as e:
                # Call error window
                self.error_window(textError=f"Something went wrong when making cog dir!\n{e}")

        # Make new cog file
        cogFile = open(f"{start}{self.currentFilePath}/cogs/{self.fileName}", "w")
        cogFile.write(pure_input)
        cogFile.close()

        # Closes textbox window
        self.doneWindow()

app = mainApp()
app.title("Cogs Manager")
app.geometry("600x600")
app.mainloop()