import discord
import random

from discord.ext import commands
from commands import cmd_elpotato, cmd_ping, cmd_8ball, cmd_clear, cmd_subreddit
from events import member_join, member_remove, ready

potato = commands.Bot(command_prefix='!el ')


@potato.event
async def on_member_join(member):
    member_join.event(member)


@potato.event
async def on_member_remove(member):
    member_remove.event(member)


@potato.event
async def on_ready():
    ready.event()


@potato.command()
async def patato(ctx):
    await cmd_elpotato.run(ctx)


@potato.command()
async def ping(ctx):
    await cmd_ping.run(ctx, potato.latency)


@potato.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    await cmd_8ball.run(ctx, question)


@potato.command()
async def clear(ctx, amount=5):
    await cmd_clear.run(ctx, amount)


@potato.command()
<<<<<<< HEAD
async def subreddit(ctx, *, topic):
=======
async def sr(ctx, *, topic):
>>>>>>> 229e0975072216b75ff22aee8cd46191e7300a4c
    await cmd_subreddit.run(ctx, topic)
