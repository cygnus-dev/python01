import praw
import os
import discord
from random import randint


async def run(ctx, topic):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USERAGENT")

    random_index = randint(1, 100)
    subreddit = reddit.subreddit(topic)
    submissions = subreddit.hot(limit=random_index)
    submission = last_submission(submissions)
    author_name = submission.author.name

    embed = discord.Embed(
        color=discord.Colour.orange(),
        title="***REDDIT***",
        description=submission.url
    )

    embed.set_author(name="El service")
    embed.set_image(url=submission.url)
    embed.set_footer(text="posted by u/" + author_name + ",   from r/" + topic)

    await ctx.send(embed=embed)


def last_submission(submissions):
    submission = next(submissions)
    for submission in submissions:
        pass
    return submission
