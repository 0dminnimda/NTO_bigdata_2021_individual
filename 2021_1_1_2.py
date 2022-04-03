n = int(input())

nums = list(map(int, input().split(" ")))

for i in range(n)[::-1]:
    i += 1
    for j in range(n - i):
        check = [False]*i
        try:
            for v in nums[j:j+i]:
                check[v-1] = not check[v-1]
        except IndexError:
            continue
        if all(check):
            print(i)
            exit()


"""
19
5 2 6 3 5 1 4 2 1 3 6 2 5 8 1 2 5 4 3
"""

"""
6
"""
