

import requests
from lxml import etree

import user_agent


def spider():
    number = 112925109211
    url = "https://www.fedex.com/apps/fedextrack/index.html?tracknumbers="+str(number)+"&cntry_code=cn"
    ua = user_agent.get_ua()
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "zh-CN,zh;q=0.9":"max-age=0",
        "Connection":"keep-alive",
        "Cookie":"siteDC=edc; xacc=CN; fdx_cbid=30707895801596610128179610486171; fdx_locale=zh_CN; fdx_redirect=zh-cn; level=test; Rbt=f0; bm_sz=E42CBBFD7C350FCD7383D3EB7600F9F3~YAAQFQKYQbzXhoZzAQAAeithvQhqRwIlIsNm6vATcc3xthLd/pf5uSTRKk2wQdgSWogRlwUC3AIq7Ake3LWkg3kfkdt45fcVxcmOBB3Jc++OPhF1Ly2FcowBGq7u4H5Rv6Eufca8eYvapACZBbsunvQsWPJrfxHwVNZ6SnQYvoL1omAv/1WEWqvImtshVkE=; check=true; _gcl_au=1.1.1574500718.1596610113; AMCVS_1E22171B520E93BF0A490D44%40AdobeOrg=1; s_ecid=MCMID%7C90712194857431225222661332572281436443; _abck=B1C45F4D48B14C8D3305C5AF04D9D2F8~0~YAAQJAKYQTN0BaFzAQAAtlNhvQQ3Njno2drrH/k6KJ/SUG6oLdIyz9xZrTJev1bgGFcXg8lPa2OHUzSIC6TM9tLCI7QdZlhyba0IuzGI/IhiraIOWyToOYJoMAW+l00NtohuPc8Qh3JHJ/QmEhznrVTQmpvpoaNGgOEN8m6DDlcNbYFITAn/mf2BM8TF7NL9GCkX5JKts+/K0yoHV/PCoDEKg1fMx39NwHrpfxnztIM7u1BkepjnERawQrWk31Xb+x2Z6oEzGfDx/rUIvaoqCi1wUIbihlCxtMFyd6+lF4qyxGodIR4Kj7lKlCqCKb5kpJmSl3X9~-1~-1~-1; Nina-nina-fedex-session=%7B%22locale%22%3A%22zh_cn%22%2C%22lcstat%22%3Afalse%7D; tracking_locale=zh_CN; isTablet=false; isMobile=false; isWireless=false; mbox=PC#ae3d3430a8224280b920163da73c008d.38_0#1659855718|session#a0c84e0ae64c495cbd4cf39c339cbaf2#1596619421; AMCV_1E22171B520E93BF0A490D44%40AdobeOrg=1075005958%7CMCIDTS%7C18480%7CMCMID%7C90712194857431225222661332572281436443%7CMCAAMLH-1597222361%7C11%7CMCAAMB-1597222361%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1596624761s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.1; aemserver=Prod-c0016054.prod.cloud.fedex.com; ak_bmsc=C6F6C5AEA9F2FDB5F846E614F96BD27DB83366F4E50A00006B732A5FA1102A63~pl6W9BJbNmfVJPObG+Y65rgQQ17Zxx0ED2IAtHn7d6GpvfzidOCfbVWpu+S58lVkaofqfJDFuTcFzpBb5ahAbh7sfuo59fkZh4MrQrUg+VCMQgzPHjuOnCDpS+PNU/MFZ4Wh7O1ofG/WqUSLv2SxpnG2+IE6OERRJIF8oER5fZjumVohitJI2F4K5M79Bj8XUfHKTi6ny2O6y+gYXxJmG6K6TKSWzQDeHZt2Ijb6sBTCszK1pDdn2qi9lYyKR0gRls; bm_sv=436BDA07331A325EC8496EECB261F162~Xam+qnMsIvOK4svfIdTYe9MeUU3xmeYpJYhbSX2a1YxYljiFnly1pFDdkRbC83hYFdoEMp1Y7szq20VU6sbHQDErj4sXgTW0aWEBRaLzBPqGEmF1Ws8nyroHhEpHxN6ktmn1YZfb2hLCK+P79nKid//S5W4sX0JtLsslO+ZTzoI=; s_pers=%20s_vnum%3D1596643200763%2526vn%253D1%7C1596643200763%3B%20s_dfa%3Dfedexglbl%252Cfedexapac%7C1596619961164%3B%20gpv_pageName%3Dcn%252Fzh%252Ffedex%252Funified%252Ftrackdetailspage%7C1596619996844%3B%20s_nr%3D1596618196849-New%7C1628154196849%3B%20s_invisit%3Dtrue%7C1596619996857%3B; s_sq=%5B%5BB%5D%5D; s_sess=%20s_ppv%3Dcn%252Fzh%252Ffedex%252Funified%252Funifiedtracking%252C100%252C62%252C1077%3B%20setLink%3D%3B%20s_visit%3D1%3B%20SC_LINKS%3D%3B%20s_cc%3Dtrue%3B",
        "Host":"www.fedex.com",
        "Referer":"https://www.fedex.com/zh-cn/tracking.html/",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":ua
    }
    res1 = requests.get(url,headers=headers)
    print(res1.content.decode("utf-8"))
    res2 = etree.HTML(res1.content.decode("utf-8"))
    # print(res2)

spider()