import requests
import discord
from textwrap import wrap

URL = 'https://some-random-api.ml/lyrics?title='


async def run(ctx, song):
    r = requests.get(url=URL+song)
    data = r.json()
    res = len(data['lyrics'].split())

    # if int(res) < 1000:
    #     embed1 = discord.Embed(
    #         color=discord.Colour.dark_orange(),
    #         # title=data['title'],
    #         description=f"by {data['author']}"
    #     )
    #
    #     embed1.add_field(name=data['title'], value=data['lyrics'])
    #     await ctx.send(embed=embed1)
    # else:
    x = wrap(data['lyrics'], 1000)
    embed2 = discord.Embed(
        color=discord.Colour.dark_orange(),
        # title=data['title'],
        description=f"by {data['author']}"
    )

    embed2.add_field(name=data['title'], value=x[0])

    embed3 = discord.Embed(
        color=discord.Colour.dark_orange(),
        # title=data['title'],
        description=f"by {data['author']}"
    )

    embed3.add_field(name=data['title'], value=x[1])

    embed4 = discord.Embed(
        color=discord.Colour.dark_orange(),
        # title=data['title'],
        description=f"by {data['author']}"
    )

    embed4.add_field(name=data['title'], value=x[2])

    # embed5 = discord.Embed(
    #     color=discord.Colour.dark_orange(),
    #     # title=data['title'],
    #     description=f"by {data['author']}"
    # )
    #
    # embed5.add_field(name=data['title'], value=x[3])
    #
    # embed6 = discord.Embed(
    #     color=discord.Colour.dark_orange(),
    #     # title=data['title'],
    #     description=f"by {data['author']}"
    # )
    #
    # embed6.add_field(name=data['title'], value=x[4])

    await ctx.send(embed=embed2)
    await ctx.send(embed=embed3)
    await ctx.send(embed=embed4)
    await ctx.send(embed=embed5)
    await ctx.send(embed=embed6)
