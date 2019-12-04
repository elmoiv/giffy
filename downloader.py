import requests, colors

def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True, headers= {'User-Agent': 'Mozilla/5.0'})
        total = int(response.headers.get('content-length'))
        downloaded = 0
        for data in response.iter_content(chunk_size = max(int(total / 1000), 1024**2)):
            f.write(data)
            downloaded += len(data)
            percent = int((downloaded / total) * 100)
            colors.print_info('Downloading: ', '{}%'.format(percent), start='\r', end='\r')
        print()
