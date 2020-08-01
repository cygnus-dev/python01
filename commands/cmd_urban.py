import urbandictionary

UD_DEFINE_URL = 'http://api.urbandictionary.com/v0/define?term='


async def run(ctx, term):
    define = urbandictionary._get_urban_json(term)

    await ctx.send(define)


