import discord

from discord.ext import commands
from commands import cmd_ping
from events import member_join, member_remove, ready

potato = commands.Bot(command_prefix='!')


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
async def ping(ctx):
    await cmd_ping.run(ctx)
