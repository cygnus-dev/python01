import praw
import os
import discord

from random import randint


async def run(ctx):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USER_AGENT")

    random_index = randint(1, 50)
    memes_subreddit = reddit.subreddit("memes")
    submissions = memes_subreddit.hot(limit=random_index)
    submission = last_submission(submissions)
    author_name = submission.author.name
    submission_title = submission.title
    submission_link = submission.url
    upvotes = submission.ups

    embed = discord.Embed(
        color=discord.Colour.dark_orange(),
        title="***MEME***",
        description=":arrow_double_up: : " + str(upvotes)
    )

    embed.set_author(url=submission_link, name=submission_title)
    embed.set_image(url=submission_link)
    embed.set_footer(text="posted on r/memes " + " posted by u/" + author_name)

    await ctx.send(embed=embed)


def last_submission(submissions):
    submission = next(submissions)
    for submission in submissions:
        pass
    return submission
