# -*- coding: UTF-8 -*-
from requests_html import HTMLSession
import requests
import time
import random
import http.client
import socket

url = 'https://tianqi.qq.com/'
def getHtmlSource(url, data=None):
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        # # "Cookie": "pgv_pvid=9893669030; RK=ttq4glzaNu; ptcz=bd6ec59545cb182c82a1b499f9f552a54c195f39373fc4bdd94355b195eabbad; eas_sid=v1O6R327Y3E306T4e7p5z3i6F2; fqm_pvqid=16b2d941-4f1e-4494-856e-592d55c740ae; tvfe_boss_uuid=30c81d91206bed1a; pac_uid=1_1353097778; LW_uid=C1E6I411L3D839v802s893V5C5; ied_qq=o1291474449; uin_cookie=o1291474449; iip=0; LW_sid=C1L6h4Y3g417q3G0X059U0H0n4; _tc_unionid=3b0be06f-a68a-4ed2-ab8b-a7730226364f; o_cookie=1353097778; luin=o1353097778; lskey=00010000303b40aaf5b28bc8c9dd2c2a1f636089b08f0e7b19a3881a7a7b27ec044ed1e98b7a842c6e9f03fe; wxunionid=; psrf_qqopenid=21F10F83D4E12143F6A38E271847B45F; wxopenid=; psrf_qqrefresh_token=B07A26BE44343C4171E96B4FFD758175; tmeLoginType=2; wxrefresh_token=; euin=oKokoinq7iSlNn**; qqmusic_key=Q_H_L_5T6oKSlorHZ2L-Ked_ZlFNPenj7kYuCGGN6EXfOUwBU-yq2P9LV7tDQ; psrf_qqaccess_token=FA86543BC35F3AFEF9DE6DE1042B76AD; psrf_musickey_createtime=1650533899; psrf_access_token_expiresAt=1658309899; uin=1353097778; qm_keyst=Q_H_L_5T6oKSlorHZ2L-Ked_ZlFNPenj7kYuCGGN6EXfOUwBU-yq2P9LV7tDQ; psrf_qqunionid=9AB0C0EC64FE552D953195FD9E201558; pgv_info=ssid=s9627175095; ts_last=tianqi.qq.com/; ts_refer=www.baidu.com/link; ts_uid=4152523940",
        "Host": "tianqi.qq.com",
        "Referer": "https://www.baidu.com/link?url=s31cFbpYNeAx0j4GA_IqxoV3wfb5ROMcEq6TK8y5Ot3&wd=&eqid=d4b15b2400000d18000000046262254f",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"
    }
    timeout = random.randint(80, 180)
    while True:
        try:
            session = HTMLSession()
            response = session.get(url, headers=header, timeout=timeout)
            response.html.render(timeout=200)
            # response.encoding = 'gb2312'
            break
        except socket.timeout as e:
            print('Timeout:', e)
            time.sleep(2)
        except socket.error as e:
            print('Socket error', e)
            time.sleep(2)

        except http.client.BadStatusLine as e:
            print('BadStatusLine', e)
            time.sleep(2)

        except http.client.IncompleteRead as e:
            print('Incomplete read', e)
            time.sleep(2)
    return response.html.html
with open('./sourceHtml.txt',mode='x',encoding='utf-8') as f:
    f.write(getHtmlSource(url))
    f.close