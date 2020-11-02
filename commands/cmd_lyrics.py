import requests
import discord
from textwrap import wrap

URL = 'https://some-random-api.ml/lyrics?title='


async def run(ctx, song):
    r = requests.get(url=URL+song)
    data = r.json()
    res = len(data['lyrics'])

    x = wrap(data['lyrics'], 1000)

    if int(res) < 1000:
        embed2 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=f"by {data['author']}"
        )

        embed2.add_field(name=data['title'], value=x[0])
        await ctx.send(embed=embed2)
    elif 1000 < int(res) < 2000:
        embed2 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=f"by {data['author']}, seperated into different messages cause length"
        )

        embed2.add_field(name=data['title'], value=x[0])

        embed3 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[1]
        )

        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)

    elif 2000 < int(res) < 3000:

        embed2 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=f"by {data['author']}, seperated into different messages cause length"
        )

        embed2.add_field(name=data['title'], value=x[0])

        embed3 = discord.Embed(
            color=discord.Colour.dark_orange(),

            description=x[1]
        )

        embed4 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[2]
        )

        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
        await ctx.send(embed=embed4)

    elif 3000 < int(res) < 4000:
        embed2 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=f"by {data['author']}, seperated into different messages cause length"
        )

        embed2.add_field(name=data['title'], value=x[0])

        embed3 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[1]
        )

        embed4 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[2]
        )

        embed5 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[3]
        )

        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
        await ctx.send(embed=embed4)
        await ctx.send(embed=embed5)
    elif 4000 < int(res) < 5000:
        embed2 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=f"by {data['author']}, seperated into different messages cause length"
        )

        embed2.add_field(name=data['title'], value=x[0])

        embed3 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[1]
        )

        embed4 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[2]
        )

        embed5 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[3]
        )

        embed6 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[4]
        )

        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
        await ctx.send(embed=embed4)
        await ctx.send(embed=embed5)
        await ctx.send(embed=embed6)

    elif 5000 < int(res) < 6000:
        embed2 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=f"by {data['author']}, seperated into different messages cause length"
        )

        embed2.add_field(name=data['title'], value=x[0])

        embed3 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[1]
        )

        embed4 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[2]
        )

        embed5 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[3]
        )

        embed6 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[4]
        )

        embed7 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[5]
        )

        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
        await ctx.send(embed=embed4)
        await ctx.send(embed=embed5)
        await ctx.send(embed=embed6)
        await ctx.send(embed=embed7)

    else:
        embed2 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=f"by {data['author']}, seperated into different messages cause length"
        )

        embed2.add_field(name=data['title'], value=x[0])

        embed3 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[1]
        )

        embed4 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[2]
        )

        embed5 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[3]
        )

        embed6 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[4]
        )

        embed7 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[5]
        )

        embed8 = discord.Embed(
            color=discord.Colour.dark_orange(),
            description=x[6]
        )

        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
        await ctx.send(embed=embed4)
        await ctx.send(embed=embed5)
        await ctx.send(embed=embed6)
        await ctx.send(embed=embed7)
        await ctx.send(embed=embed8)
