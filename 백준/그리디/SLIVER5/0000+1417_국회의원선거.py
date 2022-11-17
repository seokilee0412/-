N = int(input())
vote_per_person = [int(input()) for _ in range(N)]
vote_other = vote_per_person[1:]
dasom = vote_per_person[0]
count = 0
vote_other.sort(reverse=True)
if len(vote_per_person) == 1:
        count = 0
else:
    while dasom <= vote_other[0]:
        dasom += 1
        vote_other[0] -= 1
        count += 1
        vote_other.sort(reverse=True)
print(count)

# 10 20 10 10 => 16 14 10 10  (max - dasom // 2) + 1
# 10 20 20 20 => 16 14 20 20 (6) = > 19 14 17 20 (3) = > 20 14 17 19 (1) = > 10
# 10 20 20 20 => 13 19 19 19 (3) = > 16 18 18 18 (3) => 19 17 17 17 (3) -> 9