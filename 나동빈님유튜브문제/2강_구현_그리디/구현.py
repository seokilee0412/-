# 상하좌우


def move():
    n = int(input())
    x, y = 1, 1
    plans = input().split()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:

        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

    print(x, y)


# 시각
def check_three():
    h = int(input())

    count = 0
    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1

    print(count)

# 왕실의 나이트

def knight_move():
    input_data = input()
    row = int(input_data[1])
    column = int(ord(input_data[0])) - int(ord('a')) + 1

    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1,2), (-1,2), (-2, 1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
            result += 1
    print(result)

# 문자열 재정렬

def sorting_string():
    data = input()
    result = []
    value = 0

    for x in data:
        if x.isalpha():
            result.append(x)
        else:
            value += int(x)
    result.sort()
    if value != 0:
        result.append(str(value))
    print(''.join(result))