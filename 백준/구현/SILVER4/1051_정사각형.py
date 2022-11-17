N, M = map(int, input().split())

row = [input() for _ in range(N)]

min_lengths = min(N, M)

result = 0
column_index = 0
for row_index in range(N):
    for column_index in range(M):
        for min_length in range(min_lengths):
            if row_index + min_length  < N and column_index + min_length  < M:
                first_value = row[row_index][column_index]
                second_value = row[row_index + min_length][column_index]
                third_value = row[row_index][column_index + min_length ]
                fourth_value = row[row_index + min_length][column_index + min_length]
                if first_value == second_value == third_value == fourth_value:
                    result = max(result, (min_length +1) ** 2)
print(result)
        
    # if N > M:
    #     second_value = row[row_index + max_length -1][column_index]
    #     if first_value == second_value:
    #         thrid_value = row[row_index][column_index + max_length - 1]
    # else:
    #     second_value = row[row_index][column_index + max_length - 1]
        

