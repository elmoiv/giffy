# For each key in data

# KEY: Provider name
#
# VALUES:
#     * re: tuple of (0, 1): 0: regex to match url validity
#                            1: index to get ID of the gif that we will need to name files
#
#     * op: A direct url that can use "ID" from "re" to download source directly
#
#     * ext: extension of file
#           - main: gif --> will be downloaded directly
#           - else: mp4, webm, ... --> will be passed to ffmpeg to be converted to gif
#
#     * scrape: if not None, then we add a script that can get url from HTML
#              - Will be passed to eval()
#              - Prefered to be short and efficent

# 15 Providers
data = \
{
    'Giphy':{
        're': (r'((http|https):\/\/)?(www\.)?giphy\.com\/gifs\/(([a-z-]+)(?<=-))?([a-zA-Z0-9-]+)', 6),
        'op': 'https://media.giphy.com/media/{}/source.gif',
        'ext': 'gif',
        'scrape': None
    },
    'Tenor':{
        're': (r'((http|https):\/\/)?(www\.)?tenor\.com\/view\/(.*)(?=-)-gif-(\d+)', 4),
        'op': None,
        'ext': 'gif',
        'scrape': 'soup.find("meta",  {"property":"og:image"})["content"]'
    },
    'Tenor : Source':{
        're': (r'((http|https):\/\/)?media\d\.tenor\.co\/images\/([a-f0-9]+)\/tenor\.gif', 3),
        'op': None,
        'ext': 'gif',
        'scrape': 'url_input'
    },
    'Gfycat':{
        're': (r'((http|https):\/\/)?(www\.)?gfycat\.com\/([a-z-]+)', 4),
        'op': None,
        'ext': 'gif',
        'scrape': 'soup.find("meta",  {"property":"og:url"})["content"]'
    },
    'Reaction GIFs':{
        're': (r'((http|https):\/\/)?(www\.)?reactiongifs\.com\/([a-z0-9-]+)', 4),
        'op': None,
        'ext': 'gif',
        'scrape': 'soup.find("meta",  {"property":"og:image"})["content"]'
    },
    'GIFbin':{
        're': (r'((http|https):\/\/)?(www\.)?gifbin\.com\/(\d+)', 4),
        'op': None,
        'ext': 'mp4',
        'scrape': 'soup.find("source",  {"type":"video/mp4"})["src"]'
    },
    'Imgflip':{
        're': (r'((http|https):\/\/)?(www\.)?imgflip\.com\/gif\/([a-z0-9]+)', 4),
        'op': 'https://i-download.imgflip.com/{}.gif',
        'ext': 'gif',
        'scrape': None
    },
    'Tumblr':{
        're': (r'((http|https):\/\/)?\w+\.tumblr\.com\/post\/(\d+)', 3),
        'op': None,
        'ext': 'gif',
        'scrape': 'soup.find("meta",  {"property":"og:image"})["content"][:-1]'
    },
    'Twitter':{
        're': (r'((http|https):\/\/)?(www\.)?twitter\.com\/(.*)(?<=status\/)(\d+)', 5),
        'op': None,
        'ext': 'mp4',
        'scrape': '"https://video.twimg.com/tweet_video/"+soup.find("meta",'
                  '{"property":"og:image"})["content"][:-4].split("/")[-1]+".mp4"'
    },
    'Imgur':{
        're': (r'((http|https):\/\/)?i\.imgur\.com\/([A-Za-z0-9]+)', 3),
        'op': None,
        'ext': 'mp4',
        'scrape': 'soup.find("meta",  {"property":"og:video"})["content"]'
    },
    'Imgur : Source':{
        're': (r'((http|https):\/\/)?(www\.)?imgur\.com\/(gallery|\w)\/([a-z]+\/)?([A-Za-z0-9]+)', 6),
        'op': None,
        'ext': 'mp4',
        'scrape': 'url_input'
    },
    'Reddit':{
        're': (r'((http|https):\/\/)?((www|old)\.)?reddit\.com\/r\/(.*)(?<=comments\/)([a-z0-9_\/]+)', 6),
        'op': None,
        'ext': 'gif',
        'scrape': r'''(re.search(r'https:\/\/preview.redd.it\/([a-z0-9]+).gif\?s=[a-f0-9]+','''
                   '''requests.get(url_input+".json", headers={'User-Agent': 'Mozilla/5.0'}).text)).group(0)'''
    },
    '9GAG':{
        're': (r'((http|https):\/\/)?(www\.)?9gag\.com\/\w+\/([A-Za-z0-9]+)', 4),
        'op': 'https://img-9gag-fun.9cache.com/photo/{}_460sv.mp4',
        'ext': 'mp4',
        'scrape': None
    },
    'Sizzle':{
        're': (r'((http|https):\/\/)?(www\.)?onsizzle\.com\/i\/([A-Za-z0-9-]+)(?=-)-([a-f0-9]+)', 4),
        'op': None,
        'ext': 'mp4',
        'scrape': 'soup.find("source",  {"type":"video/mp4"})["src"]'
    },
    'PANA.GIFS':{
        're': (r'((http|https):\/\/)?(www\.)?panagif\.com\/gif\/([A-Za-z0-9-]+)', 4),
        'op': None,
        'ext': 'gif',
        'scrape': 'soup.find("source",  {"type":"image/gif"})["src"]'
    },
    'Gifer':{
        're': (r'((http|https):\/\/)?(www\.)?gifer\.com(\/\w\w)?\/([A-Za-z0-9]+)', 5),
        'op': 'https://i.gifer.com/embedded/download/{}.gif',
        'ext': 'gif',
        'scrape': None
    },
    'TikTok':{
        're': (r'((http|https):\/\/)?(www\.)?tiktok\.com\/@(.*)(?<=video\/)(\d+)', 5),
        'op': None,
        'ext': 'mp4',
        'scrape': 'soup.find("video")["src"]'
    }
}
