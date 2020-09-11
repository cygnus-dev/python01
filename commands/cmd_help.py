import discord


async def run(ctx):

    embed = discord.Embed(
        color=discord.Color.dark_blue(),
        title="***HELP***"
    )

    embed.add_field(name="__**working cmds**__", value='''`help(this one)`
                                                    `rarded`
                                                    `pp {user}`
                                                    `bf`
                                                    `ok`
                                                    `whois {user}`
                                                    `die`
                                                    `urban {word}`
                                                    `potatos {amount}`
                                                    `meme`
                                                    `subreddit {subr}`
                                                    `clear {amount}`
                                                    `8ball {question}`
                                                    `ping`
                                                    `patato`''')

    embed.add_field(name="__*in progress cmds*__", value='''`stick_bug`
                                                        `genius`''')

    await ctx.send(embed=embed)
