def recursiveSum(l):
    if len(l) == 1:
        return l[0]
    return l[0] + recursiveSum(l[1:])
