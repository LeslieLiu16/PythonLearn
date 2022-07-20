import urllib.request

url = 'https://weibo.com/5642544204'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': 'PC_TOKEN=a976cdb6ca; XSRF-TOKEN=WGwliZsvcYFER-k6dqUFeV8p; login_sid_t=816d6bfe662ca6e032cbd932819f60c4; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=1733789676739.672.1658062490895; SINAGLOBAL=1733789676739.672.1658062490895; ULV=1658062490899:1:1:1:1733789676739.672.1658062490895:; ALF=1689598528; SSOLoginState=1658062528; SUB=_2A25P0HaQDeRhGeNI71AU9CrOyziIHXVspO9YrDV8PUNbmtB-LWb6kW9NSGSkqyFOtFrSQsgLJEE1WXzBBgRF_IkV; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWwGR8ipp_XbN0DR-NqAfhu5JpX5KzhUgL.Fo-cShzfShBEehB2dJLoIpie9PSjIgHeIP-LxKBLBonLBoqt; WBPSESS=pjKBJSZW10avonQ3aiCIXAgFU_uKZsgtCrT5C0PVEjszAl0uYC_8kMyD6xNqtrtHgNucxcUelL7p3-kj7QV6j7WahXzeBJiBKiB6CKQhsxhffKy6dsNSw_MdT-IE2j-xAFVa2f6qWNCoia6UI1_Ddg==',
    'referer': 'https://weibo.cn/',
    'dnt': '1',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)
