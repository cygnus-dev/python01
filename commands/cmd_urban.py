import urbandictionary as ud


async def run(ctx, term):
    defs = ud.define(term)

    await ctx.send(defs.url)
