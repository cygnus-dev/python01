import discord

from discord.ext import commands
from commands import cmd_elpotato
from events import member_join, member_remove, ready

potato = commands.Bot(command_prefix='!el')


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
async def pootato(ctx):
    await cmd_elpotato.run(ctx)
