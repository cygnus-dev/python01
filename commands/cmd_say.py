import discord


async def run(ctx, input):
    await ctx.channel.purge(limit=1)
    await ctx.send(input)
