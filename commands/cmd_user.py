import discord
from discord import embeds


async def run(ctx, display_name):
    members = ctx.guild.members

    member = next((m for m in members if m.display_name == display_name), None)
    member_avatar = member.avatar_url
    member_id = member.id
    member_sjoin_date = member.joined_at.day
    member_sjoin_year = member.joined_at.year
    member_sjoin_month = member.joined_at.month
    member_sjoin_time = str(member_sjoin_date) + "/" + str(member_sjoin_month) + "/" + str(member_sjoin_year)
    member_discrimination = member.discriminator
    account_create_day = member.created_at.day
    account_create_month = member.created_at.month
    account_create_year = member.created_at.year
    account_create_time = str(account_create_day) + "/" + str(account_create_month) + "/" + str(account_create_year)

    embed = discord.Embed(
        color=discord.Colour.dark_blue(),
        title="Member doesn't exist" if member is None else member.name,
        description=""
    )

    embed.set_thumbnail(url=member_avatar)
    embed.add_field(name="User ID", value=member_id)
    embed.add_field(name="Joined server at", value=member_sjoin_time)
    embed.add_field(name="Discrimination", value=member_discrimination)
    embed.add_field(name="Account created at", value=account_create_time)

    await ctx.send(embed=embed)
