import re, os, requests, data, converter, downloader
from scraper import extract_url, check_url
from colors import Printer

websites = data.data
convert = converter.convert
download = downloader.download

# Run Printer
log = Printer()

def main(url_input, optimize_gif=False, enable_logging=True):
    # Enable or disable logging
    log.LOG = enable_logging

    try:
        log.print_info('Analyzing: ', url_input)

        # Apply scheme to avoid error
        if 'http' not in url_input:
            url_input = 'https://' + url_input

        GIF_RES = None

        for one in websites:
            child = websites[one]

            r, idx = child['re']

            # Check if url matches an existed provider
            if re.match(r, url_input):

                log.print_info('Provider: ', one)
                log.print_info('Optimzation: ', 'ON' * optimize_gif + 'OFF' * (not optimize_gif))

                # Getting ID to use as a name for the GIF
                ID = re.split(r, url_input)[idx].replace('/', '-')

                # If scrape is True
                # We perform a given script via eval() to get media url
                if child['scrape']:
                    log.print_info('Scraping: ', 'In Progress...')
                    GIF_RES = extract_url(url_input, child['scrape'])
                else:
                    log.print_info('Scraping: ', 'Skipped')
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
                log.print_info('Converting: ', 'In Progress...')
                convert(name, optimize_gif)
            else:
                log.print_info('Converting: ', 'Skipped')

            # Clean downloaded videos after converting
            if name.split('.')[-1] != 'gif':
                os.remove(name)

            log.print_info('Result: ', 'Success!')
            return

        log.print_error('Result: ','Provider is not supported :(')
        return

    except KeyboardInterrupt:
        log.print_error('Result: ', 'Interrupted!')

if __name__ == '__main__':
    main(input('URL: '), True, True)
