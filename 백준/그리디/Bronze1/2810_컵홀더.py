N = int(input())
place_info = input()
count = 0
for p in place_info:
    if 'L' in p:
        count +=1
if count < 4:
    print(len(place_info))
else:
    minus_cup = (count // 2 - 1)
    print(len(place_info) - minus_cup)