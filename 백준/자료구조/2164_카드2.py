import sys
input = sys.stdin.readline
from collections import deque
# 제일 위 카드 버림 
# 그 다음 제일 위에 있는 카드 제일 밑으로
# 하나 남을 때까지 반복

N = int(input())

queue = deque()
for i in range(1, N+1):
    queue.append(i)
while len(queue) > 1:
    queue.popleft()

    num = queue.popleft()
    queue.append(num)

print(queue[0])