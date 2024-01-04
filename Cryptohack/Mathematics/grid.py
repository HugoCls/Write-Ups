import requests

burp0_url = "https://web.ctflearn.com:443/grid/controller.php?action=add_point"
burp0_cookies = {"_ga": "GA1.2.1345249428.1695990195", "_gid": "GA1.2.1850077107.1695990195", "PHPSESSID": "qvkdnc91nbg6ndrmhejke154v5"}
burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36", "Origin": "https://web.ctflearn.com", "Content-Type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://web.ctflearn.com/grid/index.php", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"}

burp0_data = {"x": [x for x in range(1,500)], "y": [y for y in range(1,500)]}

r = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

print(r)

print(r.text)