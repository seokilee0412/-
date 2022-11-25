import sys
from collections import deque, defaultdict
input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    queue = deque()
    num_dict = defaultdict(int)
    for i in range(len(numbers)):
        queue.append([i, numbers[i]])
        num_dict[numbers[i]] += 1
    num_dict = {k:v for k,v in sorted(num_dict.items(), key=lambda x:x[0], reverse=True)}
    count = 0
    stop = False
    for k in num_dict:
        num_of_k = num_dict.get(k)
        same_count = 0
        while True:
            if queue[0][0] == M and queue[0][1] == k:
                result.append(count + 1)
                stop = True
                break
            elif queue[0][1] == k:
                queue.append(queue.popleft())
                count += 1
                same_count += 1
                if same_count == num_of_k:
                    break
            else:
                queue.append(queue.popleft())
        if stop:
            break

for r in result:
    print(r)