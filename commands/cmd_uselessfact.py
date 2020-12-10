import requests
import discord
import time

URL = 'https://uselessfacts.jsph.pl/random.json?language=en'


async def run(ctx):
    test_msg = "ah yes"
    compile_msg = await ctx.send('`compiling python... /`')
    for i in range(10):
        await compile_msg.edit(content="`compiling python... \`")
        time.sleep(0.25)
        await compile_msg.edit(content="`compiling python... /`")
        time.sleep(0.25)
    r = requests.get(url=URL)
    data = r.json()

    embed = discord.Embed(
        color=discord.Colour.dark_purple(),
        title=data['text']
    )
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)
