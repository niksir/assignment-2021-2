coords = [[-1, 3],
          [4, 3],
          [2, 1],
          [-1, -2],
          [3, -3]]

x = 1
y = 0

def get_gcd(a, b):
    if (b == 0):
        return a
    return get_gcd(b, a % b)


def getReducedForm(dy, dx):
    g = get_gcd(abs(dy), abs(dx))

    # get sign of result
    sign = (dy < 0) ^ (dx < 0)

    if (sign):
        return (-abs(dy) // g, abs(dx) // g)
    else:
        return (abs(dy) // g, abs(dx) // g)


def findAll(points, N, xO, yO):
    st = dict()

    for element in range(N):
        # get x and y co-ordinate of current point
        curX = points[element][0]
        curY = points[element][1]

        temp = getReducedForm(curY - yO, curX - xO)

        # if this slope is not there in set,
        # increase ans by 1 and insert in set
        if (temp not in st):
            st[temp] = []

    return st



def minLinesToCoverPoints(points, N, xO, yO):
    st = dict()
    minLines = 0
    res = findAll(points, N, xO, yO)
    for i in range(N):
        curX = points[i][0]
        curY = points[i][1]
        temp = getReducedForm(curY - yO, curX - xO)
        if (temp in res):
            cell = [points[i][0], points[i][1]]
            res[temp].append(cell)
        if (temp not in st):
            st[temp] = 1
            minLines += 1
    return res


if __name__ == '__main__':


    print(list(minLinesToCoverPoints(coords, len(coords), x, y).values()))
    result = list(minLinesToCoverPoints(coords, len(coords), x, y).values())
    for i in result:
        print(str(i) + "\n")
