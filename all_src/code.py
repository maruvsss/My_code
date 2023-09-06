
h = {
    'Connection': 'keep-alive',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Accept-Encoding': 'gzip, deflate, br'
    }

s = requests.session()
s.headers = h
s.proxies = {'http': 'http://127.0.0.1:10809', 'https': 'https://127.0.0.1:10809'}

def get_video_url(url):
    """
    获取tiktok视频，返回下载地址
    :param url: t.co短链接
    :return:
    """
    res = s.get(url=url, timeout=18)
    video_url = re.search('\"downloadAddr\":\"(.+?)\"', res.text).group(1)
    return video_url.replace('\\u0026', '&') if len(video_url)!=0 else None

def download(video_url):
    """
    下载视频
    :param video_url: tiktok视频链接
    """
    h1 = h.copy()
    h1['Referer'] = 'https://www.tiktok.com/'
    h1['Accept-Encoding'] = 'identity;q=1, *;q=0'
    h1['Range'] = 'bytes=0-'
    res = s.get(video_url, headers=h1)
    file_name = str(datetime.datetime.now().strftime('%y%m%d%H%M'))+'.mp4'
    with open('.\\'+file_name,'wb') as f:
        f.write(res.content)
    return f.name