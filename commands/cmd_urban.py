
import requests
import discord

URL = 'http://api.urbandictionary.com/v0/define?term='


async def run(ctx, word):
    r = requests.get(url=URL+word)
    data = r.json()

    if len(data['list']) > 0:
        define = data['list'][0]

        embed = discord.Embed(
            color=discord.Colour.dark_blue(),
            title=f'**define {word}**'
        )

        embed.add_field(name="Definition", value=define['definition'])
        embed.add_field(name="Example", value=define['example'])

        await ctx.send(embed=embed)
    else:
        await ctx.send(f'```No results for {word}```')
