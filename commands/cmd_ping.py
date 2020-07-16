async def run(ctx, latency):
    await ctx.send(f'pong! {round(latency * 1000)}ms')
