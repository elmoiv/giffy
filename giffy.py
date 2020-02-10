import re, os, requests, data, converter, downloader
from scraper import extract_url, check_url
from colors import print_error, print_info

websites = data.data
convert = converter.convert
download = downloader.download

def main(url_input, optimize_gif=False):
    print_info('Analyzing: ', url_input)

    # Apply scheme to avoid error
    if 'http' not in url_input:
        url_input = 'https://' + url_input

    GIF_RES = None

    for one in websites:
        child = websites[one]

        r, idx = child['re']

        # Check if url matches an existed provider
        if re.match(r, url_input):

            print_info('Provider: ', one)
            print_info('Optimzation: ', 'ON' * optimize_gif + 'OFF' * (not optimize_gif))

            # Getting ID to use as a name for the GIF
            ID = re.split(r, url_input)[idx].replace('/', '-')

            # If scrape is True
            # We perform a given script via eval() to get media url
            if child['scrape']:
                print_info('Scraping: ', 'In Progress...')
                GIF_RES = extract_url(url_input, child['scrape'])
            else:
                print_info('Scraping: ', 'Skipped')
                # if not scrape, then we perform direct download
                # using "op" key in data.py
                GIF_RES = child['op'].format(ID)

        else:
            continue

        # Full name with extension
        name = '{}.{}'.format(ID, child['ext'])

        # Check if url is connectable
        check_url(GIF_RES)

        # Download mp4/GIF
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

    print_error('Result: ','Provider is not supported :(')
    return

def dl(a, b=False):
    try:
        main(a, b)
    except KeyboardInterrupt:
        print_error('Result: ', 'Interrupted!')

# if file is executed rather than imported
if __name__ == '__main__':
    dl(input('URL: '), True)
