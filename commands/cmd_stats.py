import psutil
import os
import platform

async def run(ctx):
    cpufreq = psutil.cpu_freq()
    uname = platform.uname()
    svmem = psutil.virtual_memory()
    await ctx.send(f"Total cores: {psutil.cpu_count(logical=False)}")
    await ctx.send(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    await ctx.send(f"Total meroy: {get_size(svmem.total)}")
    await ctx.send(f"available memroy: {get_size(svmem.available)}")
    # await ctx.send(f"System: {uname.system}")
    # await ctx.send(f"Node Name: {uname.node}")
    # await ctx.send(f"Release: {uname.release}")
    # await ctx.send(f"Version: {uname.version}")
    # await ctx.send(f"Machine: {uname.machine}")
    # await ctx.send(f"Processor: {uname.processor}")
    # await ctx.send(cpu_usage)
    # await ctx.send(core_count)
    # await ctx.send(stats)

def get_size(bytes, suffix="B"):
    #copied code, and copied with absolotuly no shame
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor