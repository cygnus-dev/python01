import discord
import os
import settings


from discord.ext import commands


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("bot is working!")


@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server')


@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


bot.run(os.getenv("TOKEN"))
