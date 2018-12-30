import tkinter as tk
from tkinter import ttk

class mainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Button Style
        style = ttk.Style()
        style.configure("BW.TLabel", font=('tahoma','24', 'bold'), background="white")
        # Main Label
        self.welcomeText = ttk.Label(self, text="Cogs Manager", style="BW.TLabel")
        self.welcomeText.pack()
        # Make Command Label
        self.commandLabel = tk.Label(self, text="Command Maker", font=('tahoma', '14'))
        self.commandLabel.place(x=145,y=50)
        # Cog Label
        self.cogLabel = tk.Label(self, text="Cog Name:", font=('tahoma', '12'))
        self.cogLabel.place(x=30, y=80)
        # Command Cog Name
        self.command_name_ = tk.StringVar()
        self.command_name = tk.Entry(self, textvariable=self.command_name_)
        self.command_name.place(x=100, y=80)
        # Button to initate new command
        self.makeCommand = tk.Button(text="Submit", font=('tohoma', '10'), command=self.openTextBox)
        self.makeCommand.place(x=165,y=110)

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
        self.cogLabel = tk.Label(self, text=f"Current Cog Name: {self.fileName}", font=('tohoma', '10'))
        self.cogLabel.place(x=10, y=70)
        # Make text box to edit custom commands
        self.textBox = tk.Text(self, width=50,height=25)
        self.textBox.place(x=22,y=100)

app = mainApp()
app.title("Cogs Manager")
app.geometry("400x600")
app.mainloop()