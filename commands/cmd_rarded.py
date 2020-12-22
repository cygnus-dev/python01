import praw
import os
import discord

from random import randint


async def run(ctx):
    await ctx.send("`processing...`")
    submissions = get_submission()
    submission = last_submission(submissions)
    await ctx.channel.purge(limit=1)
    await send_meme(ctx, submission)


def last_submission(submissions):
    submission = next(submissions)
    non_video_submission = submission
    for submission in submissions:
        if not submission.is_video:
            non_video_submission = submission
        pass
    return non_video_submission


def get_submission():
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USER_AGENT")

    random_index = randint(1, 150)
    memes_subreddit = reddit.subreddit("okbuddyretard")
    return memes_subreddit.hot(limit=random_index)


async def send_meme(ctx, submission):
    embed = discord.Embed(
        color=discord.Colour.dark_orange(),
        description=f':arrow_double_up: : {submission.ups}'
    )
    embed.set_author(url=submission.shortlink, name=submission.title)
    embed.set_footer(text=f'posted on r/memes    |    by u/{submission.author.name}')
    embed.set_thumbnail(url="https://styles.redditmedia.com/t5_2qjpg/styles/communityIcon_aek5xr5qwj051.png")
    if submission.selftext_html is None:
        embed.set_image(url=submission.url)
    else:
        embed.add_field(name=submission.title, value=submission.selftext)
    await ctx.send(embed=embed)