import praw
import os
import random
import discord
from random import randint


async def run(ctx, topic):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USERAGENT")
    random_index = randint(1, 100)
    submissions = reddit.subreddit(topic).hot(limit=random_index)

    embed = discord.Embed(
        Color=0xff4500,
        title="***REDDIT***",
        description=(last_submission(submissions)).url
    )

    embed.set_author(name="El service")
    embed.set_image(url=(last_submission(submissions)).url)

    await ctx.send(embed=embed)


def last_submission(submissions):
    submission = next(submissions)
    for submission in submissions:
        pass
    return submission
