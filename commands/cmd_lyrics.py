import requests
import discord
from textwrap import wrap

URL = 'https://some-random-api.ml/lyrics?title='


async def run(ctx, song):
    r = requests.get(url=URL+song)
    data = r.json()
    res = len(data['lyrics'])

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

    if int(res) < 1000:
        embed2 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=f"by {data['author']}"
        )

        embed2.add_field(name=data['title'], value=x[0])
        await ctx.send(embed=embed2)
    elif 1000 < int(res) < 2000:
        embed2 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=f"by {data['author']}, seperated into different messages cause length"
        )

        embed2.add_field(name=data['title'], value=x[0])
        # await ctx.send(embed=embed2)

        embed3 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=x[1]
        )

        # embed3.add_field(name=data['title'], value=x[1])
        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
    elif 2000 < int(res) < 3000:
        embed2 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=f"by {data['author']}, seperated into different messages cause length"
        )

        embed2.add_field(name=data['title'], value=x[0])
        # await ctx.send(embed=embed2)

        embed3 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=x[1]
        )

        # embed3.add_field(name=data['title'], value=x[1])
        # await ctx.send(embed=embed3)
        embed4 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=x[2]
        )

        # embed4.add_field(name=data['title'], value=x[2])
        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
        await ctx.send(embed=embed4)
    elif 3000 < int(res) < 4000:
        embed2 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=f"by {data['author']}, seperated into different messages cause length"
        )

        embed2.add_field(name=data['title'], value=x[0])
        # await ctx.send(embed=embed2)

        embed3 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=x[1]
        )

        # embed3.add_field(name=data['title'], value=x[1])
        # await ctx.send(embed=embed3)
        embed4 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=x[2]
        )

        # embed4.add_field(name=data['title'], value=x[2])
        # await ctx.send(embed=embed4)
        embed5 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=x[3]
        )

        # embed5.add_field(name=data['title'], value=x[3])
        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
        await ctx.send(embed=embed4)
        await ctx.send(embed=embed5)
    else:
        embed2 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=f"by {data['author']}, seperated into different messages cause length"
        )

        embed2.add_field(name=data['title'], value=x[0])
        # await ctx.send(embed=embed2)

        embed3 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=x[1]
        )

        # embed3.add_field(name=data['title'], value=x[1])
        # await ctx.send(embed=embed3)
        embed4 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=x[2]
        )

        # embed4.add_field(name=data['title'], value=x[2])
        # await ctx.send(embed=embed4)
        embed5 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=x[3]
        )

        # embed5.add_field(name=data['title'], value=x[3])
        # await ctx.send(embed=embed5)
        embed6 = discord.Embed(
            color=discord.Colour.dark_orange(),
            # title=data['title'],
            description=x[4]
        )

        # embed6.add_field(name=data['title'], value=x[4])
        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
        await ctx.send(embed=embed4)
        await ctx.send(embed=embed5)
        await ctx.send(embed=embed6)
    # await ctx.send(embed=embed2)
    # await ctx.send(embed=embed3)
    # await ctx.send(embed=embed4)
    # await ctx.send(embed=embed5)
    # await ctx.send(embed=embed6)
