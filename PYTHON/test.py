from collections import OrderedDict
hour_list = [8, 10, 12, 14, 16, 18, 20, 22, 0, 2, 4, 6]
test_data = {
    '24.07': 'test1',
    '25.07': 'test1'
}
hour_collection = OrderedDict()

for hour in hour_list:
    new_dict = hour_collection.setdefault(hour, dict())
    new_dict.setdefault('24.07', 'ok')


for key, value in hour_collection.items():
    print(key, value)