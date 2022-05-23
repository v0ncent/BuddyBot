# Vincent Banks
# ---BuddyBot DeveloperTules---

# ---imports---
# discord libraries
import discord.ext.commands
from discord.ext import commands

# project files
from main import buddy_bot


class DeveloperTules(commands.Cog):
    def __init__(self, buddybot):
        self.buddybot = buddybot

    # when cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('DeveloperTools Online')

    # load command
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        buddy_bot.load_extension(f'cogs.{extension}')
        await ctx.send(f"{extension} has been loaded")

    # unload command
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        buddy_bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f"{extension} has been loaded")

    # shutdown command
    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.bot.logout()
        print('shutting down')


def setup(buddybot):
    buddybot.add_cog(DeveloperTules(buddybot))
