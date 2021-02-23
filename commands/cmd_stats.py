import psutil

async def run(ctx):
    cpu_usage = psutil.cpu_percent
    core_count = psutil.cpu_count
    await ctx.send(cpu_usage)
    await ctx.send(core_count)