import praw
import os
import discord

from random import randint


async def run(ctx):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USERAGENT")

    random_index = randint(1, 50)
    memes_subreddit = reddit.subreddit("memes")
    submissions = memes_subreddit.hot(limit=random_index)
    submission = last_submission(submissions)
    author_name = submission.author.name

    embed = discord.Embed(
        color=discord.Colour.orange(),
        title="***MEME***",
        description=submission.url
    )

    embed.set_author(name="El service")
    embed.set_image(url=submission.url)
    embed.set_footer(text="posted by u/" + author_name + ",  from r/memes")

    await ctx.send(embed=embed)


def last_submission(submissions):
    submission = next(submissions)
    for submission in submissions:
        pass
    return submission
