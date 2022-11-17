X = int(input())

# find_n =
n = 0
while True:
    n += 1
    sum_n = (n * (n+1)) / 2
    if X - sum_n <= 0:
        n -= 1
        break
if n%2 == 1:
    sum_n = (n * (n+1)) / 2
    up_down_sum = X - sum_n
    result = str(int(up_down_sum )) + '/' + str(int(n + 2 - up_down_sum))
else:
    sum_n = (n * (n+1)) / 2
    up_down_sum = X - sum_n
    result = str(int(n+2 - up_down_sum)) + '/' + str(int(up_down_sum ))
print(result)