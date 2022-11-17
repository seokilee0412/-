import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
customer_dict = defaultdict(list)
for _ in range(N):
    age, name = input().split()
    age = int(age)
    customer_dict[age].append(name)

sorted_customer_dict = {k:v for k,v in sorted(customer_dict.items(), key=lambda x:x[0])}

for k,v in sorted_customer_dict.items():
    for val in v:
        print(k, val)
