import discord
from discord import embeds


async def run(ctx, user):
    user_name = ctx.message.guild.members(user)

    embed = discord.Embed(
        color=discord.Colour.dark_orange(),
        title=user_name,
        description=""
    )

    await ctx.send(embed=embed)
