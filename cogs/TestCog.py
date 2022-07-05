from discord.ext import commands


class TestCog(commands.Cog):
    def __init__(self, buddybot):
        self.buddybot = buddybot


def setup(buddybot):
    buddybot.add_cog(TestCog(buddybot))
