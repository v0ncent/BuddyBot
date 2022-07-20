from discord.ext import commands


class TestCog(commands.Cog):
    def __init__(self, buddybot):
        self.buddybot = buddybot

    @commands.command()
    async def test(self, ctx):
        await ctx.send('test')


def setup(buddybot):
    buddybot.add_cog(TestCog(buddybot))
