#재귀적 구현
from bisect import bisect


def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)

# 반복문 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)

# 파이썬 이진 탐색 라이브러리
'''
bisect_left(a, x)
정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
가장 왼쪽 인덱스 : 동일한 값이 존재할 경우 가장 첫 번째 인덱스
동일한 값 없으면 해당 값보다 작은 값의 인덱스 + 1
bisect_right(a, x)
정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
가장 오른쪽 인덱스 : 동일한 값이 존재할 때 가장 마지막 인덱스 + 1
동일한 값 없으면 해당 값의 인덱스 + 1
'''
#값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))

