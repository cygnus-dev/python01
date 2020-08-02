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
    author_name = submission.author.name
    submission_title = submission.title
    submission_link = submission.shortlink
    up_votes = submission.ups
    subreddit_icon = subreddit.collections.subreddit.community_icon

    embed = discord.Embed(
        color=discord.Colour.dark_orange(),
        title="***REDDIT***",
        description=":arrow_double_up: : " + str(up_votes)
    )

    embed.set_author(url=submission_link, name=submission_title)
    embed.set_image(url=submission.url)
    embed.set_footer(text="posted on r/" + topic + "   |    by u/" + author_name)
    embed.set_thumbnail(url=str(subreddit_icon))

    await ctx.send(embed=embed)


def last_submission(submissions):
    submission = next(submissions)
    for submission in submissions:
        pass
    return submission
