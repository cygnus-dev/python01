import praw
import os
import discord
from random import randint


async def run(ctx):
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                         user_agent="USER_AGENT")

    random_index = randint(1, 50)
    subreddit = reddit.subreddit('askreddit')
    submissions = subreddit.hot(limit=random_index)
    submission = last_submission(submissions)

    embed = discord.Embed(
        color=discord.Colour.dark_orange(),
        title="***REDDIT***",
        description=f':arrow_double_up: {submission.ups}'
    )

    comment_list = submission.num_comments
    comment_index = randint(1, comment_list)
    all_comments = submission.comments._comments(limit=comment_index)
    comment = last_comment(all_comments)

    embed.add_field(name='what', value=submission.comments.body)

    await ctx.send(embed=embed)


def last_submission(submissions):
    submission = next(submissions)
    non_video_submission = submission
    for submission in submissions:
        if not submission.is_video:
            non_video_submission = submission
        pass
    return non_video_submission


def last_comment(all_comments):
    comment = next(all_comments)
    for comment in all_comments:
        pass
    return comment
