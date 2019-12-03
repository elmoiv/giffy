import re, os, requests, data, scraper, converter, downloader
from colors import print_error, print_info

websites = data.data
convert = converter.convert
download = downloader.download

def dl(url_input, optimize_gif=False):
    # Last "/" not needed
    if url_input[-1] == '/':
        url_input = url_input[:-1]

    GIF_RES = None

    for one in websites:
        child = websites[one]

        r, idx = child['re']

        # Check if url matches existed provider
        if re.match(r, url_input):

            print_info('Detected: ', one)
            # Getting ID to use as a name for the GIF
            ID = re.split(r, url_input)[idx]

            # If scrape is True
            # We perform a given script via eval() to get media url
            if child['scrape']:
                print_info('', 'Scraping...')
                page = requests.get(url_input).text
                soup = scraper.b(page)
                GIF_RES = eval(child['scrape'])
            else:
                # if not scrape, then we perform direct download
                # using "op" key in data.py
                GIF_RES = child['op'].format(ID)

        else:
            continue
        
        # Full name with extension
        name = '{}.{}'.format(ID, child['ext'])

        # Using requests.head to check if file exists without downloading
        # https://stackoverflow.com/a/41546847/5305953
        if requests.head(GIF_RES).status_code != 200:
            print_error('Error: ', 'Correct media type not found!')
            return

        print_info('Downloading: ', name)
        download(GIF_RES, name)

        if child['ext'] != 'gif':
            print_info('', 'Converting MP4 to GIF...')
            convert(name, optimize_gif)

        # Clean downloaded videos after converting
        if name.split('.')[-1] != 'gif':
            os.remove(name)

        print_info('', 'GIF Saved!')
        return

    print_error('Error: ','Provider is not supported :(')
    return