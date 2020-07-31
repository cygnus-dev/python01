import urbandictionary
from urbandictionary import UrbanDefinition, _get_urban_json, _parse_urban_json, define

UD_DEFINE_URL = 'http://api.urbandictionary.com/v0/define?term='


async def run(ctx, term):

    define(term)

    await ctx.send(define(term))
