from giffy import dl
import os

urls = '''https://twitter.com/ChartBTS/status/1201920311245099008
https://www.reddit.com/r/gif/comments/e4gmow/karate_move/
https://ronweasley.tumblr.com/post/188896662009
https://giphy.com/gifs/mlb-astros-houston-carlos-correa-SxMF64Np2fUCMlcUdE
https://tenor.com/view/beyond-scared-straight-scared-straight-gif-13451841
https://imgur.com/gallery/RGLR9DK
https://9gag.com/gag/aMYdqjX
https://onsizzle.com/i/worlc-star-hip-hop-com-worlg-star-there-goes-that-cellphone-4484cfdb1cfc4453b78f46017c721183
https://gfycat.com/artisticheftygoldenmantledgroundsquirrel-good-job
http://www.gifbin.com/985660
http://www.reactiongifs.com/george-costanza-omg-2/
https://imgflip.com/gif/3i39e4
https://gifer.com/en/1Ibj
http://panagif.com/gif/XTDYDAGEc/'''.split('\n')

os.makedirs('GIFS', exist_ok=True)
os.chdir('GIFS')

for url in urls:
    dl(url, True)
    print()
