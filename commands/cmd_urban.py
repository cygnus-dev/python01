import urbandictionary

UD_DEFINE_URL = 'http://api.urbandictionary.com/v0/define?term='


async def run(ctx):
    define = urbandictionary.random()[0]
    await ctx.send(define.word + "\n" + define.definition + "\n" + define.example)


