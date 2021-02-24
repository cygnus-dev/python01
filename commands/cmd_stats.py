import psutil
import os
import platform
import GPUtil
#pip3 install tabulate, gputil

async def run(ctx):
    cpufreq = psutil.cpu_freq()
    uname = platform.uname()
    svmem = psutil.virtual_memory()
    await ctx.send(f"Total cores: {psutil.cpu_count(logical=False)}")
    await ctx.send(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    await ctx.send(f"Total meroy: {get_size(svmem.total)}")
    await ctx.send(f"available memroy: {get_size(svmem.available)}/ Used: ({svmem.percent}%)")
    

def get_size(bytes, suffix="B"):
    #copied code, and copied with absolotuly no shame
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor