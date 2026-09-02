from collections import deque


def minMoves(classroom, energy):
    m = len(classroom)
    n = len(classroom[0])

    litter = {}
    count = 0
    start = None

    for i in range(m):
        for j in range(n):
            if classroom[i][j] == 'L':
                litter[(i, j)] = count
                count += 1
            elif classroom[i][j] == 'S':
                start = (i, j)

    if count == 0:
        return 0

    all_litter = (1 << count) - 1

    queue = deque()
    queue.append((start[0], start[1], energy, 0))

    visited = set()
    visited.add((start[0], start[1], energy, 0))

    moves = 0

    while queue:

        for _ in range(len(queue)):
            r, c, e, mask = queue.popleft()

            if mask == all_litter:
                return moves

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):

                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                if e == 0:
                    continue

                ne = e - 1
                nmask = mask

                if classroom[nr][nc] == 'L':
                    nmask |= 1 << litter[(nr, nc)]

                if classroom[nr][nc] == 'R':
                    ne = energy

                state = (nr, nc, ne, nmask)

                if state not in visited:
                    visited.add(state)
                    queue.append(state)

        moves += 1

    return -1


classroom = []

m = int(input())

for _ in range(m):
    classroom.append(input().strip())

energy = int(input())

print(minMoves(classroom, energy))