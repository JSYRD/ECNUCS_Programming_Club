import requests
import re
headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
# "Cookie": "BAIDU_SSP_lcr=https://www.baidu.com/link?url=nL-uWujJDiObCCNKtj1scafCtS-fINsLHsWXI2D5miJj8DrqgPeYzYCG62NyKGHC&wd=&eqid=9b782bd70001aa4e000000046262415b; userId=eyJpdiI6IlJOSUoyTm0zNWJZK0pVeXVNN2QxdHc9PSIsInZhbHVlIjoiRFJvSmtuSlJzSDVEbmJhUnErOGFSdW5kV2M1bnVLV2d4XC82cXVaeHNZMGVLUllEdkoxT3hLM0hUUnh2V0Y3RjQwd2NMeEF1OW9YWnkyc1p5RGl2dmdBPT0iLCJtYWMiOiIzYTYxZTY2ZmRlZjU1ZjAyMmEzNzc4Y2VjY2UxNzRkYTNhYmRmMzk3OWM5YzgwZDM4YWUxZjBmZDA1ODc0YTE3In0%3D; is_refresh=eyJpdiI6IlhcL0hzZWNWWWtVKzhycG8xcnJjODdBPT0iLCJ2YWx1ZSI6IlNhQndkTm1HNkxhamhSZnJoclFkNmc9PSIsIm1hYyI6IjUwMjAzOTNiMzg0MzhjZDgyYzVhYmQ1NDk1MjcyOWQyOWFjYzE1OTEyZmEyZWQ4ZDAyNzAyMWI5MTdhMTBkZTcifQ%3D%3D; gr_user_id=5c928f7a-be43-4902-961b-89db9a66ad4f; Hm_lvt_3b668291b682e6dc69686a3e2445e11d=1650606429; a1bb553aa9fcabf8_gr_session_id=b9af52ef-75f0-4c24-a3c2-fc04f81fd3db; a1bb553aa9fcabf8_gr_session_id_b9af52ef-75f0-4c24-a3c2-fc04f81fd3db=true; Hm_lpvt_3b668291b682e6dc69686a3e2445e11d=1650606572",
"Host": "www.jinse.com",
# "Referer": "https://www.baidu.com/link?url=nL-uWujJDiObCCNKtj1scafCtS-fINsLHsWXI2D5miJj8DrqgPeYzYCG62NyKGHC&wd=&eqid=9b782bd70001aa4e000000046262415b",
# "sec-ch-ua": " Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100",
# "sec-ch-ua-mobile": "?0",
# "sec-ch-ua-platform": "Windows",
# "Sec-Fetch-Dest": "document",
# "Sec-Fetch-Mode": "navigate",
# "Sec-Fetch-Site": "cross-site",
# "Sec-Fetch-User": "?1",
# "Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"
}

url = "https://www.jinse.com/coin/bitcoin"
response = requests.get(url)
# print(response.text)
price = re.search(r'(?<=<span>最新成交价</span>\n<span>￥)([0-9]*,)*[0-9]*.[0-9]*',response.text)
# with open('./sourceHtml.txt',mode='x', encoding='utf-8') as f:
#     f.write(response.text)
#     f.close()
print(price.group())