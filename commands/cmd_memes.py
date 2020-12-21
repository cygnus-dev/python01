import discord
import os
import praw
from random import randint
import time

NO_OF_ELEMENTS_REMOVE = 3

async def run(ctx, count):
    submissions = get_submissions(count)
    remove_admin_messages(submissions)    
    urls = get_valid_urls(submissions)
    
    memes_time = 5 * (int(count)- 3)
    
    await ctx.send(f'this commadn will go on for {memes_time} seconds')
    await send_submissions(ctx, urls)
    await ctx.send("`yeah its over`")


def get_submissions(count):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent="USER_AGENT")
    return reddit.subreddit("memes").hot(limit=int(count))


async def send_submissions(ctx, urls):
    embed = discord.Embed(color = discord.Colour.dark_orange())
    for url in urls:        
        embed.set_image(url=url)
        await ctx.send(embed=embed)
        time.sleep(5)


def remove_admin_messages(submissions):
    list_iterator = iter(submissions)
    for i in range(NO_OF_ELEMENTS_REMOVE):
        next(list_iterator)


def get_valid_urls(submissions):
    url_array = []
    for submission in submissions:
        if not (submission.is_video or submission.over_18):
            url_array.append(submission.url)
    return url_array

