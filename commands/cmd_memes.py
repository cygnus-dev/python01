import discord
import os
import praw
from random import randint

async def run(ctx):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                        user_agent="USER_AGENT")
    
    meme_subreddit = reddit.subreddit("memes")
    submissions =  meme_subreddit.hot(limit=5)
 
    for submission in submissions:
        embed = discord.Embed()
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)
