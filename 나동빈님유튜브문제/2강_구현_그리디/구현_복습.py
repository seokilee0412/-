# 상하좌우

from curses.ascii import isalpha


def move2exit():
    N = int(input())
    x, y = 1, 1
    move_path = input().split()
    
    ny = {'R' : 1, 'L' : -1, 'U' : 0, 'D' : 0}
    nx = {'R' : 0, 'L' : 0, 'U' : -1, 'D' : 1}
    for m in move_path:
        mx = x + nx[m]
        my = y + ny[m]
        if mx <= 0 or my <=0 or mx > N or my > N:
             continue
        x = mx
        y = my
    print(x, y)

# 시각

def check_time_in_three():
    time = input()
    count = 0
    for i in range(time + 1):
        for j in range(60):
            for k in range(60):
                check = str(i) + str(j) + str(k)
                if '3' in check:
                    count += 1
    print(count)

# 왕실의 나이트

def knight():
    place = input()
    row = place[1]
    column = int(ord(place[0])) - int(ord('a')) + 1
    x, y = row, column
    move_path = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    count = 0
    for m in move_path:
        mx = x + m[0]
        my = y + m[1]
        if mx >= 1 and my >= 1 and mx <= 8 and my <= 8:
            count += 1
    print(count)

# 문자열 재정렬

def sorting_string():
    check_string = input()
    string_ = []
    value_ = 0
    for c in check_string:
        if c.isalpha():
            string_.append(c)
        else:
            value_ += int(c)
    string_.sort()
    if value_ != 0:
        string_.append(value_)
    print(''.join(string_))