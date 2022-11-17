N, M = map(int, input().split())

guitar_package_one = [list(map(int, input().split())) for _ in range(M)]

guitar_package_price = []
guitar_one_by_one = []
for p, one in guitar_package_one:
    guitar_package_price.append(p)
    guitar_package_price.append(one * 6)
    guitar_one_by_one.append(one)
guitar_package_price.sort()
guitar_one_by_one.sort()

result = 0
package_buy = (N//6)
package_price = package_buy * guitar_package_price[0]
result += package_price
re = max(N - package_buy * 6, 0)
if re > 0:
    one_by_one_price = guitar_one_by_one[0]
    one_by_one_buy = re * one_by_one_price
    package_buy =  guitar_package_price[0]
    price = min(one_by_one_buy, package_buy)
    result += price
    print(result)
else:
    print(result)
