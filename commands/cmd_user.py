import discord


async def run(ctx, display_name):

    member = next((m for m in ctx.guild.members if m.display_name == display_name), None)

    if member is None:
        embed = discord.Embed(
            color=discord.Colour.dark_blue(),
            title="Member is not exist"
        )

    else:
        member_s_join_time = f'{member.joined_at.day}-{member.joined_at.month}-{member.joined_at.year}'
        account_create_time = f'{member.created_at.day}-{member.created_at.month}-{member.created_at.year}'

        embed = discord.Embed(
            color=discord.Colour.dark_blue(),
            title="Member doesn't exist" if member is None else member.name,
        )

        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="User ID", value=member.id)
        embed.add_field(name="Joined server at", value=member_s_join_time)
        embed.add_field(name="Discrimination", value=f'#{member.discriminator}')
        embed.add_field(name="Account created at", value=account_create_time)
        embed.add_field(name="status", value=member.status.name)
        embed.add_field(name="Account type", value="Bot" if member.bot else "Human")
        embed.add_field(name="Mention", value=member.mention)
        embed.add_field(name="Nick", value=member.nick)
        embed.add_field(name="Roles", value=member.roles)
        embed.add_field(name="Icon url", value=member.avatar_url)

    await ctx.send(embed=embed)
