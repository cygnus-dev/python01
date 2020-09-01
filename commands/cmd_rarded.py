import praw
import os
import discord
import random

from random import randint


async def run(ctx):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USER_AGENT")

    random_index = randint(1, 150)
    subreddit = reddit.subreddit("okbuddyretard")
    submissions = subreddit.hot(limit=random_index)
    submission = last_submission(submissions)

    embed = discord.Embed(
        color=discord.Colour.dark_orange(),
        description=f':arrow_double_up: : {submission.ups}'
    )

    embed.set_author(url=submission.shortlink, name=submission.title)
    embed.set_image(url=submission.url)
    embed.set_footer(text=f'posted on r/okbuddyretard   |    posted by u/{submission.author.name}')
    embed.set_thumbnail(
        url="https://styles.redditmedia.com/t5_74is2/styles/communityIcon_7s6ixw6m34w31.png?width=256&s=e294b8c3d87167e780ab2d7308050370d2c2c06a")

    await ctx.send(embed=embed)


def last_submission(submissions):
    submission = next(submissions)
    non_video_submission = submission
    for submission in submissions:
        if not submission.is_video:
            non_video_submission = submission
        pass
    return non_video_submission
