import praw
import os
import random

from random import randint


async def run(ctx, topic):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USERAGENT")
    random_index = randint(1, 100)
    submissions = reddit.subreddit(topic).hot(limit=random_index)
    await ctx.send(last_submission(submissions).url)


def last_submission(submissions):
    submission = next(submissions)
    for submission in submissions:
        pass
    return submission
