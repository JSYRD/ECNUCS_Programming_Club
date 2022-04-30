import requests
import re
url = "http://d1.weather.com.cn/sk_2d/101020100.html?_=1650600860280"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Cookie": "Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1650597617; f_city=%E4%B8%8A%E6%B5%B7%7C101020100%7C; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1650600793",
    "Host": "d1.weather.com.cn",
    "Referer": "http://www.weather.com.cn/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"
}
response = requests.get(url, headers=headers)
temperature = re.search(r'(?<="temp":")-?[0-9]*', response.text)
cityname = re.search(r'(?<="nameen":")[a-z]*', response.text)
questtime = re.search(r'(?<="time":")[0-9]*:[0-9]*', response.text)
print("city name:%s\ntemperature:%s\ntime:%s"%(cityname.group(),temperature.group(),questtime.group()))