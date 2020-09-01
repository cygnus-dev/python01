from PIL import Image
from gsbl.stick_bug import StickBug


async def run(ctx):
    filename = message.attachments[0].filename
    await message.attachments[0].save(filename)

    sb = StickBug(Image.open())
    video = sb.video

    await ctx.send(video)
