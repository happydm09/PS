N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]


def bomb(town_map, x, y):
    cur_plus = town_map[x][y]

    for i in range(1, M + 1):
        if 0 <= x < N and 0 <= y - i < N:
            cur_plus += town_map[x][y - i]
        if 0 <= x < N and 0 <= y + i < N:
            cur_plus += town_map[x][y + i]
        if 0 <= x + i < N and 0 <= y < N:
            cur_plus += town_map[x + i][y]
        if 0 <= x - i < N and 0 <= y < N:
            cur_plus += town_map[x - i][y]

    cur_diag = town_map[x][y]

    for i in range(1, M + 1):
        if 0 <= x + i < N and 0 <= y + i < N:
            cur_diag += town_map[x + i][y + i]
        if 0 <= x - i < N and 0 <= y - i < N:
            cur_diag += town_map[x - i][y - i]
        if 0 <= x + i < N and 0 <= y - i < N:
            cur_diag += town_map[x + i][y - i]
        if 0 <= x - i < N and 0 <= y + i < N:
            cur_diag += town_map[x - i][y + i]

    return max(cur_plus, cur_diag)


max_kill = 0
for x in range(N):
    for y in range(N):
        curr_kill = bomb(town, x, y)
        if curr_kill > max_kill:
            max_kill = curr_kill

print(max_kill)
