#!/usr/bin/env python
# coding:utf-8
import csv
import json
import requests


def track_number():
    with open("ups_track_number.txt", "r", encoding="utf-8") as f:
        return f.readlines()


def upe_spider():
    # ua = user_agent.get_ua()
    csvData = []
    headers1 = {
        # "User-Agent": ua,
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "X-XSRF-TOKEN": "CfDJ8Jcj9GhlwkdBikuRYzfhrpKLp44fWXzdmwjFyYmMMIRW4B3nEI1tJT_VZNL1Ev8CoVqI_SBkZJKv3O2UrjF7VllDHaEx1AyuZvD_DCRcvhh0xFOBGKAQ6dcNUEDNz50EOoZK7EFv1xv_whYTcevASPY"

    }
    track_list = track_number()
    for track_id in track_list:
        track_id=track_id.strip()
        postData = {
            "Locale": "en_CN",
            # "TrackingNumber": ["1Z9WV5620447004448"]
            "TrackingNumber": [track_id]
        }
        url ="https://www.ups.com/track/api/Track/GetStatus?loc=en_CN"
        resp = requests.post(url, json=postData, headers=headers1)
        respDict = json.loads(resp.content.decode("utf-8"), encoding="utf-8")
        statusCode = respDict["statusCode"]
        if statusCode == "200":
            trackDetails = respDict["trackDetails"]
            for trackDetail in trackDetails:
                tempData = []
                shipmentProgressActivities = trackDetail["shipmentProgressActivities"]
                current_info = shipmentProgressActivities[1]
                first_info = shipmentProgressActivities[-1]
                first_data = first_info["date"]
                first_time = first_info["time"]
                last_data = current_info["date"]
                last_time = current_info["time"]
                location = current_info["location"]
                activityScan = current_info["activityScan"]
                tempData.append(track_id)
                tempData.append(first_data)
                tempData.append(first_time)
                tempData.append(last_data)
                tempData.append(last_time)
                tempData.append(location)
                tempData.append(activityScan)
                csvData.append(tempData)
    with open("ups4.csv", "w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        # 先写入columns_name
        writer.writerow(["track_id", "first_data", "first_time", "last_data", "last_time", "location", "activityScan"])
        # 写入多行用writerows
        writer.writerows(csvData)


if __name__ == '__main__':
    upe_spider()
