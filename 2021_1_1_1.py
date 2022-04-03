n = int(input())
exprs = [input() for _ in range(n)]

nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

tens = ["", "", "", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"]


def from_words(args):
    result = []
    for arg in args:
        num = 0
        for word in arg.split(" "):
            try:
                num += nums.index(word)
                continue
            except ValueError:
                pass
            try:
                num += tens.index(word) * 10
                continue
            except ValueError:
                pass
            assert False, "Unreachable: unknown word"
        result.append(num)
    return result


def to_words(num):
    if num < len(nums):
        return nums[num]
    ten, num = divmod(num, 10)
    return tens[ten] + " " + nums[num]


def evaluate(expr):
    sep = " plus "
    if sep in expr:
        a, b = from_words(expr.split(sep))
        return to_words(a + b)

    sep = " minus "
    if sep in expr:
        a, b = from_words(expr.split(sep))
        return to_words(a - b)

    assert False, "Unreachable: unknown operaion"


for expr in exprs:
    print(evaluate(expr))


"""
4
twelve plus forty nine
seventy two minus seventeen
one minus one
twenty three plus sixty eight
"""

"""
sixty one
fifty five
zero
ninety one
"""
