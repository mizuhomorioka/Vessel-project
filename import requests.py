import requests

cookies = {
    'i18n-prefs': 'USD',
    'ubid-main': '134-9277681-6583808',
    'session-id-apay': '356-7191989-9624820',
    'session-id': '132-2700200-6347950',
    'session-id-time': '2082787201l',
    'skin': 'noskin',
    'session-token': 'hq2cv+Rt0hUH/qkFAWisYiDay9RiZWC7FAiGzvU/Pgv5E/oVBnsD15mHHMWFNKwzufAboYzuOt+3V+orhbTHzWTamEo+xhOYWXG1sRMEtkYwYRuf2WA8af0YtqbOwwfcTJZH/LFgTYN+r/2GMqV43BIXzUFwENR1LUaMZBtAz+PkePL40Hn95tBXJUyl+wqpZNB4vXMEBG4O49a5/zz99GjZMb7BsVLqkgD6Y8Kbe8w=',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'i18n-prefs=USD; ubid-main=134-9277681-6583808; session-id-apay=356-7191989-9624820; session-id=132-2700200-6347950; session-id-time=2082787201l; skin=noskin; session-token=hq2cv+Rt0hUH/qkFAWisYiDay9RiZWC7FAiGzvU/Pgv5E/oVBnsD15mHHMWFNKwzufAboYzuOt+3V+orhbTHzWTamEo+xhOYWXG1sRMEtkYwYRuf2WA8af0YtqbOwwfcTJZH/LFgTYN+r/2GMqV43BIXzUFwENR1LUaMZBtAz+PkePL40Hn95tBXJUyl+wqpZNB4vXMEBG4O49a5/zz99GjZMb7BsVLqkgD6Y8Kbe8w=',
    'Origin': 'https://www.amazon.com',
    'Referer': 'https://www.amazon.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

params = {
    'limit': '11',
    'prefix': 'school',
    'suggestion-type': [
        'WIDGET',
        'KEYWORD',
    ],
    'page-type': 'Search',
    'alias': 'aps',
    'site-variant': 'desktop',
    'version': '3',
    'event': 'onkeypress',
    'wc': '',
    'lop': 'en_US',
    'last-prefix': 'school ',
    'avg-ks-time': '470',
    'fb': '1',
    'session-id': '132-2700200-6347950',
    'request-id': 'HG3BS2NP6BWCP0N3GR5C',
    'mid': 'ATVPDKIKX0DER',
    'plain-mid': '1',
    'client-info': 'amazon-search-ui',
}

response = requests.get('https://completion.amazon.com/api/2017/suggestions', params=params, cookies=cookies, headers=headers)