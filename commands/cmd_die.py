import random

import discord
from discord import embeds

shit_posts = ['https://www.youtube.com/watch?v=D-UmfqFjpl0',
              'https://www.youtube.com/watch?v=C9oVVBKiWnY',
              'https://www.youtube.com/watch?v=FveF-we6lcE',
              'https://www.youtube.com/watch?v=sIlNIVXpIns',
              'https://www.youtube.com/watch?v=dWNvlyycWzQ',
              'https://www.youtube.com/watch?v=Jo-0iARNt6M',
              'https://www.youtube.com/watch?v=6G4QhXWa22c',
              'https://www.youtube.com/watch?v=E4u32rmY_CA',
              'https://www.youtube.com/watch?v=K9AY5rlosRY',
              'https://www.youtube.com/watch?v=Kg-HHXuOBlw',
              'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
              'https://youtu.be/A963X1RaRfk']


async def run(ctx):
    # embed = discord.Embed(
    #     Colour=discord.Colour.dark_blue(),
    #     title="**Death**",
    #     description=(random_shitpost())
    # )
    #
    # embed.set_author(name="wtf is dis")
    await ctx.send("```here you go ```" + random_shitpost())


def random_shitpost():
    return f'{random.choice(shit_posts)}'
