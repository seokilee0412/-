from collections import Counter
R = int(input())
main = input()
friend = int(input())
friend_list = [input() for _ in range(friend)]

score = 0
for r in range(R):
    main_s = main[r]
    for f in friend_list:
        fri_s = f[r]
        if main_s == fri_s:
            score += 1
        elif (main_s == 'R' and fri_s == 'S') or (main_s == 'S' and fri_s == 'P') or (main_s == 'P' and fri_s == 'R'):
            score += 2
max_score = 0
total_F = []
for r in range(R):
    round_F = []
    for f in friend_list:
        round_F.append(f[r])
    total_F.append(round_F)
for t in total_F:
    max_score += (2 * Counter(t).most_common(3)[0][1])
    if len(Counter(t).most_common(3)) >= 2:
        max_score += (1 * Counter(t).most_common(3)[1][1])

print(score)
print(max_score)

r = int(input())
s = input()
n = int(input())
fs = [input() for _ in range(n)]

rsp = {'R':0,'S':1,'P':2}

cs = ms = 0
for i in range(r):
    ts = [[0,'R'],[0,'S'],[0,'P']]
    for j in range(n):
        if (rsp[s[i]] + 1) % 3 == rsp[fs[j][i]]: cs += 2
        elif s[i] == fs[j][i]: cs += 1

        for t in ts:
            if (rsp[t[1]] + 1) % 3 == rsp[fs[j][i]]: t[0] += 2
            elif t[1] == fs[j][i]: t[0] += 1
    ms += max(ts)[0]
print(cs)
print(ms)