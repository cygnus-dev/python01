import praw
import os
import discord
from random import randint


async def run(ctx, topic):
    submissions = get_submission(topic)
    submission = last_submission(submissions)
    await send_submission(ctx, submission, topic)

def get_submission(topic):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USER_AGENT")

    random_index = randint(1, 200)
    subreddit = reddit.subreddit(topic)
    return subreddit.hot(limit=random_index)


def last_submission(submissions):
    submission = next(submissions)
    non_video_submission = submission
    for submission in submissions:
        if not submission.is_video:
            non_video_submission = submission
        pass
    return non_video_submission


async def send_submission(ctx, submission, topic):
    embed = discord.Embed(
        color=discord.Colour.dark_orange(),
        description=":arrow_double_up: : " + str(submission.ups)
    )
    embed.set_author(url=submission.shortlink, name=submission.title)
    embed.set_footer(text=f'posted on r/{topic}    |    by u/{submission.author.name}')
    if submission.selftext_html is None:
        embed.set_image(url=submission.url)
    else:
        embed.add_field(name=submission.title, value=submission.selftext)
    await ctx.send(embed=embed)
