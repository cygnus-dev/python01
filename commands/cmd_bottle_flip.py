import discord
from random import randint


async def run(ctx):
    random_index = randint(1, 100)
    luck = random_index
    unlucky_msg = "Too bad, landed sideways :("
    lucky_msg = "landed the right way up! nice luck"

    def bottle__flip():
        if luck > 15:
            return unlucky_msg
        else:
            return lucky_msg

    await ctx.send(bottle__flip())
