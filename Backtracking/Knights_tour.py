def knights_tour(n, row, col):
    visited = [[False]*n for i in range(n)]
    res = []
    def path_gen(path,r,c,visited,step):
        if r < 0 or c < 0 or r >= n or c >= n or visited[r][c]:
            return
        if step == n*n:
            res.append(path + f'({r},{c})')
            return   
        visited[r][c] = True
        path_gen(path + f'({r},{c}) ', r - 2, c + 1, visited, step+1)
        path_gen(path + f'({r},{c}) ', r - 2, c - 1, visited, step+1)
        path_gen(path + f'({r},{c}) ', r - 1, c + 2, visited, step+1)
        path_gen(path + f'({r},{c}) ', r - 1, c - 2, visited, step+1)
        path_gen(path + f'({r},{c}) ', r + 2, c + 1, visited, step+1)
        path_gen(path + f'({r},{c}) ', r + 2, c - 1, visited, step+1)
        path_gen(path + f'({r},{c}) ', r + 1, c + 2, visited, step+1)
        path_gen(path + f'({r},{c}) ', r + 1, c - 2, visited, step+1)
        visited[r][c] = False
    path_gen('', row, col,visited,1)
    return res

print(knights_tour(5, 2, 2))