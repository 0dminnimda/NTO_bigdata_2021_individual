import ast
import re
from dataclasses import dataclass, field
from typing import List
from __future__ import annotations


print(ast.dump(ast.parse("P(f(a),g(b,f(f(a))))", mode="eval"), indent=4))


@dataclass
class Function:
    name: str
    args: List[Function]


reserved = dict()
count = 0


def repl(match):
    global count
    count += 1
    if match.group(0) not in reserved:
        Function()


p1, p2 = input(), input()

pattern = re.compile(r"(\w+)\(((?>\w+,?)+)\)")

pattern.sub(repl, )


"""
P1 = P(x, g(y, f(x)))
P2 = P(f(y), g(b, f(f(a))))

P2: y -> z

P1 = P(x, g(y, f(x)))
P2 = P(f(z), g(b, f(f(a))))

P1: x -> f(z)

P1 = P(f(z), g(y, f(f(z))))
P2 = P(f(z), g(b, f(f(a))))

P1: z -> a

P1 = P(f(a), g(y, f(f(a))))
P2 = P(f(z), g(b, f(f(a))))

P1: y -> b

P1 = P(f(a), g(b, f(f(a))))
P2 = P(f(z), g(b, f(f(a))))

P2: z -> a

P1 = P(f(a), g(b, f(f(a))))
P2 = P(f(a), g(b, f(f(a))))
"""
