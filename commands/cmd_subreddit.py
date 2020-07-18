import praw
import os


async def run(ctx, topic):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USERAGENT")
    for submission in reddit.subreddit(topic).hot(limit=1):
        await ctx.send(submission.url)
