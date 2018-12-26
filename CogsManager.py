from tkinter import *
from tkinter import ttk
import discord
from discord.ext import commands
import sys
import os

# Initalize Window =============================================================

root = Tk()
root.title("Cogs Manager")
root.geometry("400x600")

# Tkinter styles ===============================================================

h1Style = ttk.Style()
h1Style.configure("BW.TLabel", font=("helvetica", 20))

buttonStyle = ttk.Style()
buttonStyle.configure("BW.Button", foreground="black", background="grey")

# Main Window ==================================================================

h1Label = ttk.Label(root, text="Cogs Manager", style="BW.TLabel")

h1Label.pack()

root.mainloop()
