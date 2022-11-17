
# board = input()
# result = []
# split = board.split('.')
# for i in range(len(split)):
#     if len(split[i]) % 2 == 1:
#         result = -1
#         break
#     if split[i] == '':
#         result.append('.')
#     elif len(split[i]) >= 4:
#         a_length = len(split[i])//4
#         b_length = (len(split[i]) - a_length * 4) // 2
#         result.append('AAAA' * a_length)
#         if b_length != 0:
#             result.append('BB' * b_length)
#         if i != len(split) -1:
#             result.append('.')
#     else:
#         result.append('BB')
#         if i != len(split) - 1:
#             result.append('.')
# if result == -1:
#     print(result)
# else:
#     print(''.join(result))

board = input()
segment_count = 0
result = ''
for s in board:
    if s == '.':
        segment_length = segment_count
        if segment_length % 2 == 1:
            result = -1
            break
        elif segment_count == 0:
            result += '.'
        else:
            a_length = (segment_length//4)
            b_length = (segment_length - a_length *4 )//2
            semgent_result = a_length * 'AAAA' + b_length * 'BB' + '.'
            result += semgent_result
            segment_count = 0
    else:
        segment_count += 1
segment_length = segment_count
if segment_length % 2 == 1:
    result = -1
else:
    a_length = (segment_length//4)
    b_length = (segment_length - a_length *4 )//2
    semgent_result = a_length * 'AAAA' + b_length * 'BB'
    result += semgent_result
    segment_count = 0

print(result)