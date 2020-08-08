import discord
from discord import embeds


async def run(ctx, display_name):
    members = ctx.guild.members

    member = next((m for m in members if m.display_name == display_name), None)

    embed = discord.Embed(
        color=discord.Colour.dark_orange(),
        title="Member doesn't exist" if member is None else member.name,
        description=""
    )

    await ctx.send(embed=embed)
