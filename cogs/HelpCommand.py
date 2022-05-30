# Vincent Banks
# ---BuddyBot HelpCommand---

# ---imports---
# discord libraries
import random

import discord
from discord.ext import commands

# project files
import Constants


class HelpCommand(commands.Cog):
    def __init__(self, buddybot):
        self.buddybot = buddybot

    # when cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('HelpCommand Online')

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        random_index = random.randrange(len(Constants.logos))
        embed = discord.Embed(title='List of commands',
                              description='use $help (command) for more info on usage',
                              color=ctx.author.color
                              )
        embed.set_thumbnail(
            url=Constants.logos[random_index])


        await ctx.send(embed=embed)


def setup(buddybot):
    buddybot.add_cog(HelpCommand(buddybot))
