from random import randint
import time

#배열에 10,000개의 정수를 삽입

array = []
for _ in range(10000):
    #1부터 100 사이의 랜덤한 정수
    array.append(randint(1,100))

start_time = time.time()

# 선택 정렬 프로그램 성능 측정
for i in range(len(array)):
    min_index = i   #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

#측정 종료
end_time = time.time()
#수행 시간 출력
print("선택 정렬 성능 측정:", end_time - start_time)

#배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    #1부터 100 사이의 랜덤한 정수
    array.append(randint(1,100))
# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

# 측정 종료
end_time = time.time()
# 수행 시간 출력
print("기본 정렬 성능 측정:", end_time - start_time)