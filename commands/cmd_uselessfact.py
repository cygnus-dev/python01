import requests
import discord

URL = 'https://uselessfacts.jsph.pl/random.json?language=en'


async def run(ctx):
    r = requests.get(url=URL)
    data = r.json()

    embed = discord.Embed(
        color=discord.Colour.dark_purple(),
        title=data['text']
    )

    await ctx.send(embed=embed)
