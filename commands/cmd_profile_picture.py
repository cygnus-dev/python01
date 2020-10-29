import discord


async def run(ctx, display_name):
    member = next((m for m in ctx.guild.members if m.display_name == display_name), None)

    if member is None:
        embed = discord.Embed(
            color=discord.Colour.dark_blue(),
            title=f'{display_name} was not found, try adding capitalizing or spell checking '

        )
    else:
        embed = discord.Embed(
            color=discord.Colour.dark_blue(),
            title=f'{member.name} #{member.discriminator}'
        )
        embed.set_image(url=member.avatar_url)

    await ctx.send(embed=embed)
