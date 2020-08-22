import lyricsgenius
import discord
from discord import embeds


async def run(ctx, song):
    genius = lyricsgenius.Genius("8XnXxxZQLxWDhvpjcalxgv83xFRyNm8p_tKakat7hvFIaHsCNZF-PY4ST3MSehYg")
    songs = genius.search_song(song)
    if songs is None:
        # title = "nope"
        lyrics = "song not found/cmd is broek"
    else:
        lyrics = songs.lyrics
        # title = songs.title

    embed = discord.Embed(
        colour=discord.Colour.darker_grey()
    )
    # embed.add_field(name=title, value=f'{lyrics}')
    embed.set_footer(text=f'{lyrics}')

    await ctx.send(embed=embed)

