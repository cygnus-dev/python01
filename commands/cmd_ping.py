
async def run(ctx, latency):
    await ctx.send(ping_message(latency))


def ping_message(latency):
    return f'pong! ```{calculate_latency(latency)} ms```'


def calculate_latency(latency):
    return round(latency * 1000)
