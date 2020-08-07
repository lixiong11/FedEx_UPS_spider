#!/usr/bin/env python
# coding:utf-8
import csv
import json
import requests
import user_agent
def track_number():
    with open("ups_track_number.txt", "r", encoding="utf-8") as f:
        # str1 = f.read()
        # # print("$$$",str1)
        # # print(type(str1))
        # list1 =[]
        # list1.append(str1)
        # for track_num in list1:
        #     # print(track_num)
        #     # print(type(track_num))
        #     return track_num
        # f.close()
        return f.readlines()

def ups_spider():
    ua = user_agent.get_ua()
    headers1 = {
        "User-Agent": ua,
        # "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "X-XSRF-TOKEN": "CfDJ8Jcj9GhlwkdBikuRYzfhrpKLp44fWXzdmwjFyYmMMIRW4B3nEI1tJT_VZNL1Ev8CoVqI_SBkZJKv3O2UrjF7VllDHaEx1AyuZvD_DCRcvhh0xFOBGKAQ6dcNUEDNz50EOoZK7EFv1xv_whYTcevASPY"
    }
    track_list = track_number()
    for track_id in track_list:
        track_id = track_id.strip()
        # print("tr",track_num)
        postData = {
            "Locale": "en_CN",
            # "TrackingNumber": ["1Z9WV5620447004448"]
            "TrackingNumber": [track_id]
        }
        url = "https://www.ups.com/track/api/Track/GetStatus?loc=en_CN"
        resp = requests.post(url, json=postData, headers=headers1)
        respDict = json.loads(resp.content.decode("utf-8"), encoding="utf-8")
        print(respDict)
        statusCode = respDict["statusCode"]
        if statusCode == "200":
            trackDetails = respDict["trackDetails"]
            for trackDetail in trackDetails:
                shipmentProgressActivities = trackDetail["shipmentProgressActivities"]
                csvData = []
                for activity in shipmentProgressActivities:
                    # print(activity)
                    value_list = list(activity.values())
                    # print("$$$", value_list[0], value_list[-2])
                    csvData.append(value_list[0])
                    csvData.append(value_list[-2])
                print("csvData的值", csvData)
                # print(csvData)
                #     data = activity["date"]
                #     time = activity["time"]
                #     location = activity["location"]
                #     activityScan = activity["activityScan"]
                #     csvData1=csvData.append(data)
                    # csvData2 = csvData1.append(time)
                    # print(data, time, location, activityScan)
                with open("ups.csv", "a", newline="", encoding="utf-8")as f:
                    writer = csv.writer(f)
                    writer.writerow(csvData)
                    f.close()
                    # writer.writerows([data, time, location, activityScan])
                    # for value in zip(csvData):
                    #     writer.writerow(value)

ups_spider()
