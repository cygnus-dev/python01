import discord
import requests

URL = 'https://some-random-api.ml/canvas/invertgreyscale?avatar='


async def run(ctx, img):
    r = requests.get(url=URL+img)
    data = r.json()

    ctx.send(data)

