# Vincent Banks
# ---BuddyBot HelpCommand---

# ---imports---
# discord libraries
from discord.ext import commands


class HelpCCommand(commands.Cog):
    def __init__(self, buddybot):
        self.buddybot = buddybot

    # when cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('HelpCommand Online')


def setup(buddybot):
    buddybot.add_cog(HelpCCommand(buddybot))
