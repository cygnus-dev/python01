import discord
from random import randint


async def run(ctx, inputer):
    random_number = randint(1, 50)
    number = random_number

    if int(inputer) > number:
        await ctx.send("Number too high")
    else:
        await ctx.send("Number too low")

