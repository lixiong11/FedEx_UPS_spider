# dict1 ={'date': '2020/08/05', 'time': '18:00', 'location': 'Louisville, KY, United States', 'activityScan': 'Departed from Facility', 'milestone': {'name': 'cms.stapp.inTransit', 'isCurrent': True, 'isCompleted': False}, 'isInOverViewTable': False, 'activityAdditionalDescription': None, 'trailer': '', 'isDisplayPodLink': False, 'actCode': 'DP'}
# date = dict1["date"]
# print(date)

# ['', '', '', None, {'name': 'cms.stapp.delivery', 'isCurrent': False, 'isCompleted': False}, False, None, None, False, None]
# ['2020/08/06', '0:55', 'Buffalo, NY, United States', 'Arrived at Facility', {'name': 'cms.stapp.inTransit', 'isCurrent': True, 'isCompleted': False}, False, None, '', False, 'AR']
# ['2020/08/05', '18:00', 'Louisville, KY, United States', 'Departed from Facility', None, False, None, '', False, 'DP']
# ['2020/08/05', '1:18', 'Louisville, KY, United States', 'Arrived at Facility', None, False, None, '', False, 'AR']
# ['2020/08/04', '15:40', 'Anchorage, AK, United States', 'Departed from Facility', None, False, None, '', False, 'DP']
# ['2020/08/04', '13:29', 'Anchorage, AK, United States', 'Arrived at Facility', None, False, None, '', False, 'AR']
# ['2020/08/04', '19:50', 'Chek Lap Kok, Hong Kong', 'Departed from Facility', None, False, None, '', False, 'DP']
# ['2020/07/30', '21:18', '', 'Your parcel was released by the customs agency.', {'name': 'cms.stapp.clearedCustoms', 'isCurrent': False, 'isCompleted': True}, False, None, '', False, 'VK']
# ['2020/07/30', '19:02', 'Chek Lap Kok, Hong Kong', 'Your package is in transit. We&#39;re updating plans to schedule your delivery. / The package will be forwarded to a UPS facility in the destination city.', None, False, None, '', False, 'SX']
# ['2020/07/30', '18:47', 'Chek Lap Kok, Hong Kong', 'Your package is in transit. We&#39;re updating plans to schedule your delivery.', None, False, None, '', False, 'SX']
# ['2020/07/30', '0:28', 'Chek Lap Kok, Hong Kong', 'Export Scan', None, False, None, '', False, 'EP']
# ['2020/07/30', '0:28', 'Chek Lap Kok, Hong Kong', 'Origin Scan', {'name': 'cms.stapp.shipped', 'isCurrent': False, 'isCompleted': True}, False, None, '', False, 'OR']
# ['2020/07/29', '12:17', 'Hong Kong', 'Order Processed: Ready for UPS ', {'name': 'cms.stapp.orderReceived', 'isCurrent': False, 'isCompleted': True}, False, None, '', False, 'MP']
# 每次循环的值 取第一个，取倒数第二个
