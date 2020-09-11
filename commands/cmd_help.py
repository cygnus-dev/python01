import discord
from discord import Embed


async def run(ctx):

    embed = discord.Embed(
        color=discord.Color.dark_blue(),
        title="*help*"
    )

    embed.add_field(name="*working cmds*", value="sdsd")
    embed.add_field(name="*in progress cmds*", value="yea hold on")

    await ctx.send(embed=embed)
