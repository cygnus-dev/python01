import praw
import os

<<<<<<< HEAD

=======
>>>>>>> 229e0975072216b75ff22aee8cd46191e7300a4c
async def run(ctx, topic):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USERAGENT")
<<<<<<< HEAD
    for submission in reddit.subreddit(topic).hot(limit=1):
=======
    for submission in reddit.subreddit(topic).hot(limit=2):
>>>>>>> 229e0975072216b75ff22aee8cd46191e7300a4c
        await ctx.send(submission.url)
