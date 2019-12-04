import re, os, requests, data, scraper, converter, downloader
from colors import print_error, print_info

websites = data.data
convert = converter.convert
download = downloader.download

def main(url_input, optimize_gif=False):
    print_info('Analyzing: ', url_input)
    
    # Last "/" not needed
    if url_input[-1] == '/':
        url_input = url_input[:-1]
    
    # Apply scheme to avoid error
    if 'http' not in url_input:
        url_input = 'https://' + url_input

    GIF_RES = None
    soup = None

    for one in websites:
        child = websites[one]

        r, idx = child['re']

        # Check if url matches existed provider
        if re.match(r, url_input):

            print_info('Provider: ', one)
            print_info('Optimzation: ', 'ON' * optimize_gif + 'OFF' * (not optimize_gif))

            # Getting ID to use as a name for the GIF
            ID = re.split(r, url_input)[idx].replace('/', '-')

            # If scrape is True
            # We perform a given script via eval() to get media url
            if child['scrape']:
                print_info('Scraping: ', 'In Progress...')

                if 'soup' in child['scrape']:
                    page = requests.get(url_input).text
                    soup = scraper.b(page)
                try:
                    GIF_RES = eval(child['scrape'])
                except:
                    print_error('Error: ', 'Scraper found nothing!')
                    return
            else:
                print_info('Scraping: ', 'Skipped')
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
            print_error('Error: ', 'Connection Error!')
            return

        download(GIF_RES, name)

        if child['ext'] != 'gif':
            print_info('Converting: ', 'In Progress...')
            convert(name, optimize_gif)
        else:
            print_info('Converting: ', 'Skipped')

        # Clean downloaded videos after converting
        if name.split('.')[-1] != 'gif':
            os.remove(name)

        print_info('Result: ', 'Success!')
        return

    print_error('Error: ','Provider is not supported :(')
    return

def dl(a, b=False):
    try:
        main(a, b)
    except KeyboardInterrupt:
        print_error('Result: ', 'Interrupted!')
