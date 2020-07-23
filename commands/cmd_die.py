import random

shit_posts = ['https://www.youtube.com/watch?v=D-UmfqFjpl0',
              'https://www.youtube.com/watch?v=C9oVVBKiWnY',
              'https://www.youtube.com/watch?v=FveF-we6lcE',
              'https://www.youtube.com/watch?v=sIlNIVXpIns',
              'https://www.youtube.com/watch?v=dWNvlyycWzQ',
              'https://www.youtube.com/watch?v=Jo-0iARNt6M',
              'https://www.youtube.com/watch?v=6G4QhXWa22c',
              'https://www.youtube.com/watch?v=E4u32rmY_CA',
              'https://www.youtube.com/watch?v=K9AY5rlosRY',
              'https://www.youtube.com/watch?v=Kg-HHXuOBlw',
              'https://www.youtube.com/watch?v=dQw4w9WgXcQ']


async def run(ctx):
    await ctx.send("```Here you go:```" + (random_shitpost()))


def random_shitpost():
    return f'{random.choice(shit_posts)}'
