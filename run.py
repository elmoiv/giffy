from giffy import dl
import os
from colors import print_info

urls = '''https://www.reddit.com/r/gif/comments/e4gmow/karate_move/
https://giphy.com/gifs/mlb-astros-houston-carlos-correa-SxMF64Np2fUCMlcUdE
https://tenor.com/view/beyond-scared-straight-scared-straight-gif-13451841
https://gfycat.com/artisticheftygoldenmantledgroundsquirrel-good-job
http://www.reactiongifs.com/george-costanza-omg-2/
http://www.gifbin.com/985660
https://imgflip.com/gif/3i39e4
https://ronweasley.tumblr.com/post/188896662009
https://twitter.com/ChartBTS/status/1201920311245099008
https://imgur.com/gallery/RGLR9DK'''.split('\n')

os.makedirs('GIFS', exist_ok=True)
os.chdir('GIFS')

for url in urls:
    print_info('Fetching: ', url)
    dl(url, True)
    print()
