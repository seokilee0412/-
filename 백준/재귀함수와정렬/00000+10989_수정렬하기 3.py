import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
problem_dict = defaultdict(int)
for _ in range(N):
    value = int(input())
    problem_dict[value] += 1

sorted_problem_dict = {k:v for k,v in sorted(problem_dict.items(), key=lambda x:x[0]) }

for p in sorted_problem_dict:
    count = sorted_problem_dict.get(p)
    for _ in range(count):
        print(p)

##### 위의 코드 메모리 초과!!!! 파이썬에서 append함수는 재할당이 일어나므로 메모리 많이 먹음(위의 코드와는 관계없음). sys로 하는 input이 메모리 덜 먹음
# 밑처럼 미리 만들어넣고 값을 집어넣는식으로 하면 append 처럼 재할당이 일어나지 않고 값만 거기에 넣으므로 굿
import sys
n = int(sys.stdin.readline())
b = [0] * 10001
for i in range(n):
    b[int(sys.stdin.readline())] += 1
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)