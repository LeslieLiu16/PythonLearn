import urllib.request


url = 'https://dianying.taobao.com/cityAction.json?city=110100&_ksTS=1658301939379_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true'

headers = {
    'content-encoding': ' gzip',
    'content-language': ' zh-CN',
    'content-type': ' text/html;charset=UTF-8',
    'date: Wed, 20 Jul 2022 07:25': '39 GMT',
    'eagleeye-traceid': ' 21362b1c16583019394148924ece2d',
    's': ' STATUS_NOT_EXISTED',
    'server': ' Tengine/Aserver',
    'strict-transport-security': ' max-age=31536000',
    'timing-allow-origin': ' *',
    'vary': ' Accept-Encoding',
    ':authority': ' dianying.taobao.com',
    ':method': ' GET',
    ':path': ' /cityAction.json?city=110100&_ksTS=1658301939379_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true',
    ':scheme': ' https',
    'accept': ' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-encoding': ' gzip, deflate, br',
    'accept-language': ' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': ' t=8e9ba149707867a9358c632d2a700bc0; cookie2=16856be66202772881822df4367d02b0; v=0; _tb_token_=377335e558a5b; cna=S+NOG29ODhMCASpbpzYUnsjr; tb_city=110100; tb_cityName="sbG+qQ=="; isg=BPb2GDAaiJYROXxyPf7ZvWE3Ryz4FzpRzetfC2DVbVl0o5s9yKZfYSQSu3_PCzJp; l=eBMgXf0gLWfyRKUOBO5aourza77ToLRXCsPzaNbMiInca6gl1Fdt6OCHEPzHRdtjgtCUgetrJ6F2hdnw89zdVxDDBeV-1NKmnxvO.',
    'dnt': ' 1',
    'referer: https': '//dianying.taobao.com/?spm=a1z21.3046609.city.1.32c0112amxltWK&city=110100',
    'sec-ch-ua': ' " Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': ' empty',
    'sec-fetch-mode': ' cors',
    'sec-fetch-site': ' same-origin',
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
    'x-requested-with': ' XMLHttpRequest',
}
