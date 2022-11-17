from collections import defaultdict
from math import ceil
n = int(input())

phone_record = [input().split() for _ in range(n)]
name_per_price = defaultdict(int)
name_per_time = defaultdict(int)
for time, name in phone_record:
    hour = time.split(':')[0]
    minute = time.split(':')[1]
    if hour[0] == '0':
        hour_take = int(hour[1])
    else:
        hour_take = int(hour)
    
    hour_2_minute = 60 * hour_take
    
    if minute[0] == '0':
        minute_take = int(minute[1])
    else:
        minute_take = int(minute)
    
    total_time_take = hour_2_minute + minute_take
    name_per_time[name] += total_time_take
sorted_name = {k:v for k,v in sorted(name_per_time.items(), key=lambda x:x[0])}
for n, t in sorted_name.items():
    if t <= 100:
        total_price = 10
    else:
        basic_price = 10
        over_time = t - 100
        over_price = ceil(over_time/50) * 3
        total_price = basic_price + over_price
    
    name_per_price[n] += total_price

sorted_name_per_price = {k:v for k,v in sorted(name_per_price.items(), key= lambda x:x[1], reverse=True)}

for k,v in sorted_name_per_price.items():
    print(k, v)