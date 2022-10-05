def n_queens(n):
    res = []
    board = [['.']*n for i in range(n)]
    cols = set()
    pdiags = set()
    ndiags = set()
    def gen(r):
        if r == n:
            res.append([''.join(row) for row in board])
            return
        for c in range(n):
            if c in cols or r+c in pdiags or r-c in ndiags:
                continue
            board[r][c] = 'Q'
            cols.add(c)
            pdiags.add(r+c)
            ndiags.add(r-c)
            gen(r + 1)
            board[r][c] = '.'
            cols.remove(c)
            pdiags.remove(r+c)
            ndiags.remove(r-c)
    gen(0)
    return res

print(n_queens(8))