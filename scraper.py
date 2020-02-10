import bs4, requests, re
from colors import print_error

def extract_url(url, script):
    # Will be used in data.py for website config
    url_input = url
    soup = None

    if 'soup' in script:
        try:
            page = requests.get(url).text
            soup = bs4.BeautifulSoup(page, "html.parser")
        except requests.exceptions.ConnectionError:
            print_error('Result: ', 'Connection Error!')
            exit()
    try:
        return eval(script)
    except:
        print_error('Result: ', 'Scraper found nothing!')
        exit()

def check_url(url):
    try:
        
        # Using requests.head to check if file exists without downloading
        # https://stackoverflow.com/a/41546847/5305953
        if requests.head(url).status_code != 200:
            print_error('Result: ', 'No MP4 or GIF found!')
            exit()
    
    except requests.exceptions.ConnectionError:
        print_error('Result: ', 'Connection Error!')
        exit()
