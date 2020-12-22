import requests
import discord
import time

URL = 'https://uselessfacts.jsph.pl/random.json?language=en'


async def run(ctx):
    await ctx.send('`processing`')
    r = requests.get(url=URL)
    data = r.json()

    embed = discord.Embed(
        color=discord.Colour.dark_purple(),
        title=data['text']
    )
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)
