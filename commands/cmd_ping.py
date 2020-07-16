from typing import Any, Callable


async def run(ctx, latency):
    await ctx.send(f'pong! ```{calculated_latency(latency)} ms```')


calculated_latency: Callable[[Any], int] = lambda latency: round(latency * 1000)
