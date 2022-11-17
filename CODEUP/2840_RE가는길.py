n, m = input().split()

info = {}
edge = {}

for _ in range(int(m)):
    a, b, c = input().split()
    info[str(a) + str(b)] = c
    info[str(b) + str(a)] = c
    if a in edge.keys():
        edge[a].append(b)
    else:
        edge[a] = [b]
    if b in edge.keys():
        edge[b].append(a)
    else:
        edge[b] = [a]

def re(prior_edge_list, next_edge):
    if next_edge == n:
        return 0
    else:
        start = next_edge
        min_val = 100000000
        values = []
        for e in edge[str(start)]:
            if e not in prior_edge_list:
                value = info[str(start) + str(e)]
                prior_edge_list.append(next_edge)
                # if value < min_val:
                #     min_val = value
                #     min_edge = e
                values.append( int(value) + int(re(prior_edge_list, e)) )
        return min(values)
    
print(re(['-1'], '1'))