import praw
import os
import random
import discord
from discord import embeds
from random import randint


async def run(ctx):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USERAGENT")
    random_index = randint(1, 50)
    submissions = reddit.subreddit("memes").hot(limit=random_index)

    embed = discord.Embed(
        Color=0xff4500,
        title="***MEME***",
        description="you will enjoy my meme"  ### mask a link behind the title of meme
    )

    embed.set_author(name="El service")
    embed.set_image(url=last_submission(submissions).url)

    await ctx.send(embed=embed)


def last_submission(submissions):
    submission = next(submissions)
    for submission in submissions:
        pass
    return submission
