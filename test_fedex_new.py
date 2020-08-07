import csv
import random
import requests


def track_number():
    with open("fedex_track_number.txt", "r", encoding="utf-8")as f:
        return f.readlines()


def fedex_spider():
    url = 'https://www.kuaidi100.com/query'
    tempData1 = []
    headers = {
        'Referer': 'https://www.kuaidi100.com/',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
    }
    track_list = track_number()
    for fedex_track_id in track_list:
        fedex_track_id = fedex_track_id.strip()
        start_str = "0."
        num_str = ''.join(str(random.choice("0123456789")) for _ in range(16))
        num_str = start_str + num_str
        params = {
            'type': "FedEx",
            'postid': fedex_track_id,
            'temp': num_str,
            'phone': ''}
        # time.sleep(3)
        # res_info = requests.get("https://api.proxycrawl.com/?token=uxT8xq440T_FHupqXZGTKw&url="+url, params=params, headers=headers)
        res_info = requests.get(url, params=params, headers=headers)
        json_info = res_info.json()
        list_info = json_info['data']
        # print("fedex_track_id的值", fedex_track_id)
        print("list_info", list_info)
        tempData = []
        if len(list_info) >= 3:
            current_info = list_info[0]
            end_second_info = list_info[1]
            first_info = list_info[-1]
            first_time = first_info["time"]
            current_time = current_info["time"]
            current_place = current_info["context"]
            end_second_time = end_second_info["time"]
            end_second_place = end_second_info["context"]
            tempData.append(fedex_track_id)
            tempData.append(first_time)
            tempData.append(end_second_time)
            tempData.append(end_second_place)
            tempData.append(current_time)
            tempData.append(current_place)
            tempData1.append(tempData)
        else:
            tempData.append(fedex_track_id)
            tempData1.append(tempData)
            continue


    # print("tempData1",tempData1)
    with open("fedex8.csv", "w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        # 先写入columns_name
        writer.writerow(["fedex_track_id", "first_time", "end_second_time", "end_second_place", "current_time", "current_place"])
        # 写入多行用writerows
        writer.writerows(tempData1)


fedex_spider()