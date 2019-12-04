import urllib.request, colors

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    percent = int((readsofar * 1e2 / totalsize) / 2)

    r_size = totalsize / 1024**2
    d_size = readsofar / 1024**2

    pgbar = '[{}{}] '.format('█' * percent, ' ' * (50 - percent)) + '[{0:.2f}/{1:.2f} MB]'.format(d_size, r_size)

    colors.print_info('Downloading: ', pgbar, start='\r', end='\r')

def download(url, output_path):
    # Avoid urllib.error.HTTPError: HTTP Error 403: Forbidden
    # https://stackoverflow.com/a/34957875/5305953
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'Mozilla/5.0')
    opener.retrieve(url, filename=output_path, reporthook=reporthook)
    print()
