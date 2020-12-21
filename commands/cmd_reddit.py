import discord
import os
import praw
from random import randint
import time

async def run(ctx, subreddit):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                        user_agent="USER_AGENT")
    
    meme_subreddit = reddit.subreddit(subreddit)
    submissions =  meme_subreddit.hot(limit=100)
    
    list_iterator = iter(submissions)    
    next(list_iterator)
    next(list_iterator)
    next(list_iterator)
    
    url_array = []

    for submission in submissions:
        url_array.append(submission.url)
        
    memes_time = 30 * (100 - 3)
    
    await ctx.send(f'this commadn will go on for {memes_time} seconds')
    
    for url in url_array:        
        embed = discord.Embed(
            color = discord.Colour.dark_orange()
        )
        embed.set_image(url=url)
        await ctx.send(embed=embed)
        time.sleep(30)
    
    await ctx.send("`yeah its over`")