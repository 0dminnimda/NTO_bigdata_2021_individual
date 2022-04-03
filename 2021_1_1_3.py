import time
from functools import lru_cache

dialog = input()
word_count = int(input())

words = [input() for _ in range(word_count)]
words = list(set(words))


@lru_cache(None)
def max_count(s, c):
    # print("  "*c, c, s)
    mx = -10000
    for word in words:
        if s[:len(word)] == word:
            mx = max(max_count(s[len(word):], c+1), mx)
    if mx == -10000:
        return c
    return mx


start = time.perf_counter()
result = max_count(dialog, 0)
print(time.perf_counter() - start, result)

"""
110110110111111011010010
6
110
11011
01111
1101101
11
0110
"""

"""
7
"""
