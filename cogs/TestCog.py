from discord.ext import commands

import CommandManager


class TestCog(commands.Cog):
    def __init__(self, buddybot):
        self.buddybot = buddybot

    @commands.command()
    async def test(self, ctx):
        await ctx.send('test')

    commands = []
    CommandManager.add_command(
        CommandManager.CommandObj("Test", "This is a test")
        , commands
    )


def setup(buddybot):
    buddybot.add_cog(TestCog(buddybot))
