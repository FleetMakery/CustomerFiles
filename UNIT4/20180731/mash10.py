import random

start = ['noon','loon','re','be','smosh']

mid = ['oo','ah','ting','tang','walla']

end = ['ing','bing','gu','yo','ling','ring','gooloo','uter']




for i in range(3):
    full = (random.choice(start)+random.choice(mid)+random.choice(end))
    print (full)
