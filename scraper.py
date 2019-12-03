import bs4

def b(page):
    return bs4.BeautifulSoup(page, "html.parser")