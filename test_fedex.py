import json

import requests

import user_agent


def fedex_spider():
    url = "https://www.fedex.com/trackingCal/track"
    ua = user_agent.get_ua()
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "475",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "_abck=717E2F5BBE6312BC799136D95A7C84D2~0~YAAQFQKYQT83nYZzAQAAWC0wwwQkA4fVorqktE50iEClVSOQ9EaS0tfbxJj0ELG1Q1u8JtDUMviPEYd4K7IB0hNdA3j4sRvxL/ZI3O7C4Az9trABmqKkaJvQN+Oe33vR1DlI7r/OW4D8Wn4Da3IdaGWDl+9iH72gaWcL0wZizdJHDpNesYTwF2/c7vT5l2q8KZF3wUxPr4t0VFbyeVY6XrApZZA7sUCK0FVTJ2e7yYsVPmsSLe3y1EjbTmNmUppufpcICxX2Q94zR5y9LV3+F7eLax3a+yg5KFCCkW92O1qZJ0a/Wrvs0plBB9UHXxkRUfsrbzLp~-1~-1~-1; siteDC=edc; fdx_cbid=31211212281596707884539760136221; fdx_locale=zh_CN; fdx_redirect=zh-cn; _gcl_au=1.1.730982134.1596708613; tracking_locale=zh_CN; bm_sz=AF7555DE606FB14B24EBDB378E58321E~YAAQE9zxgPjqNLtzAQAAmmOKxgita+0T24dmvo93SNudlATbV5Zj8dMicAf2ARSLFUSwBz8Xr3hh0C/GaCyoNBI02cqi0FlhXpe+f4k77AFJ87Lh6pCBlKy+zGPnwYMtZI2qgEMMmuUOJ1XxnKMe0Bvny5tj4q1nxCd73CTMtQ7fwhbdERvkSwnw4vjn0ao=; xacc=CN; bm_mi=24EE9138C2D0D7C8AAD3CCDC1C9F8EC0~aWloKVipLEGkc/2VDYb/LkwGmLN3+KBC5lFyAF16sofIbTidy3uK/hg3br6jZvKQK/uCu5YuLBLkxk2MUaXScLQ7+GXab3qT7KmFuFU2uio5KX37Gk+h3opihyZLs+H9lHcZ6QVsn55p6a+xbuoltDmMdTHkCKel+spYW/qMg5eJ95zET7swyXkpfLRGDKaeWSyhNi6ySmeqzgQB3HiRbBjkeeESwU0NxspIFszRHChj2xV/uImUOmzPBSpsmFiXx9zL6U96G2NwCvf/4UQKJbcp2/WWyLG2KnLEz1JGiUg=; ak_bmsc=3B3FED2F4781217887CD6B380755629D80F1DC13DC220000B1AE2C5F604DE441~pl0R250yzRndXxU3l7KoJjqIrRsU3HJopQfnvGXB6b9Q4BhkLVDTQiMhaAFiaRihVgPb2VJvTW8N3W7USLxoYJjplB/cihXCKW0q5VhVUqcfATZWeWYe/RXgEO+x6kGyhWzDe4vlfysMKQP1IBFUPXLF3xicvbKwEwitvmBPOiUTHRgUBugfJG021IFIKzBcuZEJGz88hPwk3fPu7PfN/EwK9S76XRKmn5Wv8XZneyudERGrCZ5yUpAJCbX7UpF7ly; Rbt=f0; Nina-nina-fedex-session=%7B%22locale%22%3A%22zh_cn%22%2C%22lcstat%22%3Afalse%7D; AMCVS_1E22171B520E93BF0A490D44%40AdobeOrg=1; AMCV_1E22171B520E93BF0A490D44%40AdobeOrg=1075005958%7CMCIDTS%7C18481%7CMCMID%7C77765380753195704283151858798790654842%7CMCAAMLH-1597371363%7C11%7CMCAAMB-1597371363%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1596773763s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.1; check=true; mbox=PC#cd141d906d7e4c6d85651a72ec22b1e2.38_0#1660011747|session#2c21b610e8824b45b77d6194a83dd556#1596768805; s_sq=fedexglbl%252Cfedexapac%3D%2526c.%2526a.%2526activitymap.%2526page%253Dcn%25252Fzh%25252Ffedex%25252Funified%25252Ftrackdetailspage%2526link%253D%2525E5%2525B1%252595%2525E5%2525BC%252580%2525E5%25258E%252586%2525E5%25258F%2525B2%2525E8%2525AE%2525B0%2525E5%2525BD%252595%2526region%253Dcontainer%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dcn%25252Fzh%25252Ffedex%25252Funified%25252Ftrackdetailspage%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.fedex.com%25252Fapps%25252Ffedextrack%25252F%25253Faction%25253Dtrack%252526trackingnumber%25253D112925110800%252526cntry_code%25253Dcn%252526locale%2526ot%253DA; s_pers=%20s_vnum%3D1596816000557%2526vn%253D1%7C1596816000557%3B%20s_nr%3D1596767007831-Repeat%7C1628303007831%3B%20s_dfa%3Dfedexglbl%252Cfedexapac%7C1596771240565%3B; s_sess=%20s_cc%3Dtrue%3B%20s_visit%3D1%3B%20SC_LINKS%3Dcn%252Fzh%252Ffedex%252Funified%252Ftrackdetailspage%255E%255E%25E5%25B1%2595%25E5%25BC%2580%25E5%258E%2586%25E5%258F%25B2%25E8%25AE%25B0%25E5%25BD%2595%255E%255Ecn%252Fzh%252Ffedex%252Funified%252Ftrackdetailspage%2520%257C%2520%25E5%25B1%2595%25E5%25BC%2580%25E5%258E%2586%25E5%258F%25B2%25E8%25AE%25B0%25E5%25BD%2595%255E%255E%3B%20s_ppv%3Dcn%252Fzh%252Ffedex%252Funified%252Ftrackdetailspage%252C100%252C69%252C2604%3B%20setLink%3D%3B; bm_sv=125B837F996310DE683EA75238213F7C~EXwYgvBGbNOwLDbFCgl+lNeSszubxUV9k2GRvriybVlcu5Ub7GF9tlFiHbUF4vXRsre+7Zvno9Op46LeIJcngxz1KMOqA4fklRXA0ykceTWKqvZGnFjEbIIjPTpUOiCCkoxeggCV9yOqIjDnbCrsuJZ4DFtkxVrs36IAohFmVHE=",
        "Host": "www.fedex.com",
        "Origin": "https://www.fedex.com",
        "Referer": "https://www.fedex.com/apps/fedextrack/?action=track&trackingnumber=112925110800&cntry_code=cn&locale=zh_CN",
        "User-Agent": ua,
        "X-Requested-With": "XMLHttpRequest"
    }
    form_data = {
        "data": {
            "TrackPackagesRequest": {"appType": "WTRK", "appDeviceType": "DESKTOP", "supportHTML": True,
                                          "supportCurrentLocation": True, "uniqueKey": "", "processingParameters": {},
                                          "trackingInfoList": [{"trackNumberInfo": {"trackingNumber": "112925110800",
                                                                                    "trackingQualifier": "",
                                                                                    "trackingCarrier": ""}}]}},
        "action": "trackpackages",
        "locale": "zh_CN",
        "version": "1",
        "format": "json"
    }
    # 'https://api.proxycrawl.com/?token=uxT8xq440T_FHupqXZGTKw&url=' +
    res1 = requests.post(url, headers=headers, data=form_data)
    print(res1)
    print(res1.content.decode("utf-8"))
    res2 = json.loads(res1.content.decode("utf-8"), encoding="utf-8")
    print(res2)

fedex_spider()