

async def run(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
