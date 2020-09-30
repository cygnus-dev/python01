import discord
import random
from discord.ext import commands
from commands import cmd_elpotato, cmd_ping, cmd_8ball, \
    cmd_subreddit, cmd_why, cmd_meme, cmd_potatos, \
    cmd_urban, cmd_die, cmd_user, cmd_bottle_flip, \
    cmd_profile_picture, cmd_rarded, cmd_genius, \
    cmd_stick_bug, cmd_clear, cmd_help, cmd_askreddit,\
    cmd_what, cmd_invite
from events import member_join, member_remove, ready

potato = commands.Bot(command_prefix='$')


@potato.remove_command('help')
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
async def subreddit(ctx, *, topic):
    await cmd_subreddit.run(ctx, topic)


@potato.command()
async def meme(ctx):
    await cmd_meme.run(ctx)


@potato.command()
async def potatos(ctx, amount=5):
    await cmd_potatos.run(ctx, amount)


@potato.command()
async def urban(ctx, word):
    await cmd_urban.run(ctx, word)


@potato.command()
async def die(ctx):
    await cmd_die.run(ctx)


@potato.command()
async def whois(ctx, *, display_name):
    await cmd_user.run(ctx, display_name)


@potato.command()
async def why(ctx):
    await cmd_why.run(ctx)


@potato.command(aliases=['bf'])
async def bottle_flip(ctx):
    await cmd_bottle_flip.run(ctx)


@potato.command(aliases=['pp'])
async def profile_picture(ctx, *, display_name):
    await cmd_profile_picture.run(ctx, display_name)


@potato.command()
async def rarded(ctx):
    await cmd_rarded.run(ctx)


@potato.command()
async def genius(ctx, *, song):
    await cmd_genius.run(ctx, song)


@potato.command()
async def stick_bug(ctx):
    await cmd_stick_bug.run(ctx)


@potato.command()
async def help(ctx):
    await cmd_help.run(ctx)


@potato.command(aliases=['ar'])
async def askreddit(ctx):
    await cmd_askreddit.run(ctx)


@potato.command()
async def what(ctx, *, inputer):
    await cmd_what.run(ctx, inputer)


@potato.command()
async def invite(ctx):
    await cmd_invite.run(ctx)
