async def run(ctx, amount):

    if amount > 250:
        await ctx.send("`250 is lmiti moron no more than that`")
    else:
        await ctx.send(":potato:" * amount)

