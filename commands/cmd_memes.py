import discord
import os
import praw
from random import randint
import time

async def run(ctx, amount):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                        user_agent="USER_AGENT")
    
    meme_subreddit = reddit.subreddit("memes")
    submissions =  meme_subreddit.hot(limit=int(amount))
    
    list_iterator = iter(submissions)    
    next(list_iterator)
    next(list_iterator)
    next(list_iterator)
    
    memes_time = 30 * int(amount)
    
    await ctx.send(f'this commadn will go on for {memes_time} seconds')
    
    for submission in submissions:        
        embed = discord.Embed(
            color = discord.Colour.dark_orange()
        )
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)
        time.sleep(30)
