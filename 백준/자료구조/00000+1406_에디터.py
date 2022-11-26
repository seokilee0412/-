import sys
input = sys.stdin.readline

prob_list = list(input().rstrip())
N = int(input())

command = [input().rstrip() for _ in range(N)]
cursor_pos = len(prob_list)
move_left = 0
move_right = 0
#L, D, B, P $
for c in command:
    if c == 'L':
        move_left += 1
    
    elif c == 'D':
        move_right += 1

    elif c == 'B':
        cursor_pos = cursor_pos - move_left + move_right
        if cursor_pos <= 0:
            cursor_pos = 0
        elif cursor_pos > len(prob_list):
            cursor_pos = len(prob_list)
        if cursor_pos != 0:
            del prob_list[cursor_pos-1]
            cursor_pos -= 1
        move_left = 0
        move_right = 0

    else:
        cursor_pos = cursor_pos - move_left + move_right
        if cursor_pos <= 0:
            cursor_pos = 0
        elif cursor_pos >= len(prob_list):
            cursor_pos = len(prob_list)
        com, add = c.split()
        prob_list.insert(cursor_pos, add)
        cursor_pos += 1
        move_left = 0
        move_right = 0

print(''.join(prob_list))


'''
위의 풀이는 시간 초과 발생
remove, insert는 O(N)이 걸릴수도 있음

따라서 O(1)가 걸리는 pop과 append만을 사용해야함 
아래는 다른 분의 풀이임
소름 돋는 풀이
'''
import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []
for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif command[0] == 'B':
        if st1:
            st1.pop()
    else:
        st1.append(command[1])
st1.extend(reversed(st2)) #reverse를 쓰면 st2가 비어있을경우 TypeError를 일으키므로 reversed를 사용
print(''.join(st1))
