# DiscordTk #
- - - - 

## Requirements ##
- - - -
* Python 3.6.6 or higher
* Discord 1.0.0a rewrite

## Installation ##
- - - -
1. git clone https://github.com/Astrol99/DiscordTk.git in command-line or download zip.
2. go into the directory where you installed DiscordTk. 
3. open command-line in that directory.
4. type your token in token entry and command prefix in command_prefix or put them in token.txt with instructions below. 

## Load token.txt setup ##
In token.txt, on the first line, replace <Put Your Discord Token Here> with your discord bot token and second line, replace <Command Prefix Here> with the command prefix with your command prefix.

##### Example #####
```
N18KJDSF89QKJSH.I2GKDSGF8723K9
!
```
NOTE: Not actual token

## Bot Setup ##
To first run your discord bot, either enter your token and prefix in the GUI and click "enter", or click "Load token.txt" to load the token and prefix from token.txt without entering them. After that, you should see bot status and statistics on the command-line. To shut your bot down, either do "<command_prefix>shutdown" in discord where your bot is or close that command-line. In discord, type "<command_prefix>help" for more info.

## Admin List ##
To add yourself to adminlist.txt, find your discord user ID. 
If your bot is already online, do "<command_prefix>idMe" to see your user id or right-click on your discord profile and click on "copy ID".
After that, in adminList.txt, you can already see some user ID's, which is mine and my friends. You may delete them if you wish.
Finally, copy + paste that user ID to addAdmin.txt and you are all set!

## Cogs Manager ##
- - - -
The CogsManager.py is an GUI that helps users add discord cogs without going through Main.py to add it and update it to local list of cogs with ease.
### IMPORTANT ###
Make sure to name your cog without adding .py extension to end of it.
#### Example: ####
Wrong Way:
```
fun.py
```
Right Way:
```
fun
```
### IMPORTANT PT.2 ###
When editing your cog in the text box, make sure to make your classname different from the filename as it would create attribute problems.
