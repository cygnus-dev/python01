import praw
import os
import discord
from random import randint


async def run(ctx):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USER_AGENT")

    random_index = randint(1, 50)
    subreddit = reddit.subreddit('askreddit')
    submissions = subreddit.hot(limit=random_index)
    submission = last_submission(submissions)

    embed = discord.Embed(
        color=discord.Colour.dark_orange(),
        title="***REDDIT***",
        description=":arrow_double_up: : " + str(submission.ups)
    )



    await ctx.send(embed=embed)


def last_submission(submissions):
    submission = next(submissions)
    non_video_submission = submission
    for submission in submissions:
        if not submission.is_video:
            non_video_submission = submission
        pass
    return non_video_submission
