import praw
import os
import discord
from random import randint


async def run(ctx, topic):
    submissions = get_submission(topic)
    submission = last_submission(submissions)

    embed = discord.Embed(
        color=discord.Colour.dark_orange(),
        description=":arrow_double_up: : " + str(submission.ups)
    )

    embed.set_author(url=submission.shortlink, name=submission.title)
    embed.set_footer(text=f'posted on r/{topic}    |    by u/{submission.author.name}')
    await ctx.channel.purge(limit=1)
    if submission.selftext_html is None:
        embed.set_image(url=submission.url)
    else:
        embed.add_field(name=submission.title, value=submission.selftext)

    if submission.over_18:
        await ctx.send("**dis over 18 ma dude**")
    else:
        await ctx.send(embed=embed)


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
