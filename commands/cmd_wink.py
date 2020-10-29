import discord
import requests

URL = 'https://some-random-api.ml/animu/wink'


async def run(ctx):
    r = requests.get(url=URL)
    data = r.json()

    await ctx.send(data['link'])
