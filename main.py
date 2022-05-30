# Vincent Banks
# Copyright Vincent Banks
# ----BuddyBot Main-----

# ---imports---

# file tools
import json
import os

# discord libraries
import discord
from discord.ext import commands

# create variables from json info
with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
    prefix = data["PREFIX"]

# create buddy_bot variable
buddy_bot = commands.Bot(  # set bot prefix and enable all gateway intents
    command_prefix=prefix,
    intents=discord.Intents.all()
)

buddy_bot.remove_command('help') # remove default help command

# load cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        buddy_bot.load_extension(f'cogs.{filename[:-3]}')


# when start up is complete
@buddy_bot.event
async def on_ready():
    print('Buddy Bot Online')
    # set buddy bot status
    await buddy_bot.change_presence(activity=discord.Game("CHANGE ME WITH WALK COMMAND"))


#---CONSTANTS---



if __name__ == '__main__':
    try:
        buddy_bot.run(token)  # bot logs in with token
    except Exception as e:
        print(f"Something went wrong.\n{e}")
