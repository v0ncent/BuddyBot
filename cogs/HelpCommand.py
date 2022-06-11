# Vincent Banks
# ---BuddyBot HelpCommand---

# ---imports---
# python libraries
import os
import random

# discord libraries
import discord
from discord.ext import commands

# project files
import Constants


def get_type():
    cog_list = []
    for cog in os.listdir('./cogs'):
        if cog.endswith('.py'):
            list.append(cog_list, cog[:-3])

    return cog_list


class HelpCommand(commands.Cog):
    def __init__(self, buddybot):
        self.buddybot = buddybot

    # when cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('HelpCommand Online')

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        print(ctx.message.author.id)
        cog_list = get_type()
        random_index = random.randrange(len(Constants.logos))
        embed = discord.Embed(title='List of commands',
                              description='use $help (command) for more info on usage',
                              color=ctx.author.color
                              )
        embed.set_thumbnail(
            url=Constants.logos[random_index])

        for index in cog_list:
            if index == "DeveloperTools":
                embed.add_field(name=index, value="test", inline=True)

        await ctx.send(embed=embed)


def setup(buddybot):
    buddybot.add_cog(HelpCommand(buddybot))
