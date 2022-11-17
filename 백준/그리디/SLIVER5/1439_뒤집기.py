string = input()
count = 0

for i in range(0, len(string) - 1):
    if string[i] != string[i + 1]:
        count += 1
print( (count +1 )//2)

