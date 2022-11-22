import sys
input = sys.stdin.readline

N = int(input())
command = input().rstrip()
plus_minus_multi_divi = ['+', '-', '*', '/']

oper = []
charcter = set()
for c in command:
    if c not in plus_minus_multi_divi:
        charcter.add(c)

sorted_charcter = sorted(list(charcter))
c2num = dict()
for c in sorted_charcter:
    num = int(input())

    c2num[c] = num

num = []
for c in command:
    if c not in plus_minus_multi_divi:
        num.append(c2num[c])
    else:
        num2 = num.pop()
        num1 = num.pop()

        if c == '+':
            num.append(num2 + num1)
        elif c == '-':
            num.append(num1 - num2)
        elif c == '*':
            num.append(num1 * num2)
        else:
            num.append(num1/num2)

print('%.2f' %num[-1])