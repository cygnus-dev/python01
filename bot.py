import discord
import random
from discord.ext import commands
from commands import cmd_elpotato, cmd_ping, cmd_8ball, \
    cmd_subreddit, cmd_why, cmd_meme, cmd_potatos, \
    cmd_urban, cmd_die, cmd_user, cmd_bottle_flip, \
    cmd_profile_picture, cmd_rarded, \
    cmd_stick_bug, cmd_clear, cmd_askreddit, \
    cmd_what, cmd_invite, cmd_wink, \
    cmd_say, cmd_greyscle, cmd_facts, cmd_lyrics, \
    cmd_clyrics, cmd_uselessfact, cmd_memes, \
    cmd_reddit

from events import member_join, member_remove, ready

potato = commands.Bot(command_prefix='$')


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
async def stick_bug(ctx):
    await cmd_stick_bug.run(ctx)


@potato.command(aliases=['ar'])
async def askreddit(ctx):
    await cmd_askreddit.run(ctx)


@potato.command()
async def what(ctx, *, inputer):
    await cmd_what.run(ctx, inputer)


@potato.command()
async def invite(ctx):
    await cmd_invite.run(ctx)


@potato.command()
async def wink(ctx):
    await cmd_wink.run(ctx)


@potato.command()
async def say(ctx, *, input):
    await cmd_say.run(ctx, input)


@potato.command()
async def greyscle(ctx, *, img):
    await cmd_greyscle.run(ctx, img)


@potato.command()
async def facts(ctx):
    await cmd_facts.run(ctx)


@potato.command()
async def lyrics(ctx, *, song):
    await cmd_lyrics.run(ctx, song)


@potato.command()
async def clyrics(ctx, *, music):
    await cmd_clyrics.run(ctx, music)


@potato.command(aliases=['uf'])
async def uselessfacts(ctx):
    await cmd_uselessfact.run(ctx)


@potato.command()
async def memes(ctx, *, count):
    await cmd_memes.run(ctx, count)


@potato.command()
async def reddit(ctx, *, subreddit):
    await cmd_reddit.run(ctx, subreddit)