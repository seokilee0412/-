
# 방법 1
D = input()
F = input()
count = 0
segment = ''
for d in D:
    segment += d
    if F in segment:
        count += 1
        segment = ''
print(count)

# 방법 2
import re

D = input()
F = input()

# find = re.findall(F, D)
# print(len(find))