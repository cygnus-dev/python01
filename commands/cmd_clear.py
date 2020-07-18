import discord
from discord.ext import commands


async def run(ctx, amount):
    await ctx.channel.purge(limit=amount)
