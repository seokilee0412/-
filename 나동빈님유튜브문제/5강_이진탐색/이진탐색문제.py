# 떡볶이 떡 만들기

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start<=end):
    total = 0
    mid = (start + end )//2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

# 졍렬된 배열에서 특정 수의 개수 구하기
#값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)