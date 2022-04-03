from functools import lru_cache
from collections import defaultdict
from copy import deepcopy
from collections import Counter


n, m = map(int, input().split(" "))

canvas = [list(input()) for _ in range(n)]
original_canvas = deepcopy(canvas)
print()

circles = defaultdict(list)


def out():
    for item in canvas:
        print("".join(item))
    print()


@lru_cache(None)
def explore(x, y):
    try:
        if canvas[x][y] != "#":
            return None
    except IndexError:
        return None

    canvas[x][y] = s
    circles[s].append((x, y))

    for x0 in range(x-1, x+2):
        for y0 in range(y-1, y+2):
            explore(x0, y0)


def fill_the_next():
    for i, row in enumerate(canvas):
        for j, v in enumerate(row):
            if v == "#":
                explore(i, j)
                return True
    return False


i = 0
while 1:
    s = str(i)
    if not fill_the_next():
        break
    out()
    i += 1


values = []
for circle in circles.values():
    mn = [1000, 1000]
    mx = [-1000, -1000]

    for point in circle:
        for i in range(2):
            mn[i] = min(point[i], mn[i])
            mx[i] = max(point[i], mx[i])

    midpoint = (mn[0] + mx[0])//2, (mn[1] + mx[1])//2
    values.append(original_canvas[midpoint[0]][midpoint[1]])


result = Counter(values)
print(result["#"], result["."])


"""
30 40
........................................
...#####.......#####.....#######........
..#######.....#.....#...#########.......
.#########....#.....#..###########......
.#########....#.....#..###########......
.#########....#.....#..###########......
.#########....#.....#..###########......
.#########.....#####...###########......
..#######..............###########......
...#####...............###########......
........................#########.......
.....#########...........#######........
....##.......##.........................
...#...........#...........#######......
..#.............#........##.......##....
.##.............##......##.........##...
.#...............#......#...........#...
.#...............#.....#.............#..
.#...............#.....#.............#..
.#...............#.....#.............#..
.#...............#.....#.............#..
.#...............#.....#.............#..
.#...............#.....#.............#..
.##.............##.....#.............#..
..#.............#.......#...........#...
...#...........#........##.........##...
....##.......##..........##.......##....
.....#########.............#######......
........................................
........................................
"""

"""
2 3
"""

quit()

canvas = [["."]*40 for _ in range(30)]

circles = [
    (5, 5, 4, True),
    (4, 17, 3, False),
    (6, 28, 5, True),
    (19, 9, 8, False),
    (20, 30, 7, False),
]

for i, row in enumerate(canvas):
    for j, v in enumerate(row):
        for i0, j0, r, is_circle in circles:
            if is_circle:
                s = 0.0
            else:
                s = r**2-r*0.25
            if s <= int((i - i0)**2 + (j - j0)**2) <= r**2+r*2:
                canvas[i][j] = "#"


for item in canvas:
    print("".join(item))
