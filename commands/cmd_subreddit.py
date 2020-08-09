import praw
import os
import discord
from random import randint


async def run(ctx, topic):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USER_AGENT")

    random_index = randint(1, 100)
    subreddit = reddit.subreddit(topic)
    submissions = subreddit.hot(limit=random_index)
    submission = last_submission(submissions)

    embed = discord.Embed(
        color=discord.Colour.dark_orange(),
        title="***REDDIT***",
        description=":arrow_double_up: : " + str(submission.ups)
    )

    embed.set_author(url=submission.shortlink, name=submission.title)
    embed.set_image(url=submission.url)
    embed.set_footer(text=f'posted on r/{topic}    |    by u/{submission.author.name}')
    embed.set_thumbnail(url=str(subreddit.collections.subreddit.community_icon))

    await ctx.send(embed=embed)


def last_submission(submissions):
    submission = next(submissions)
    for submission in submissions:
        pass
    return submission
