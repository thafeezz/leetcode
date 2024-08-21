"""
notes:
    use BFS over DFS here
    BFS will explore level by level, if we start from all treasures, we can expand out and mark all land that is 1 distance, 2 distance, 3 distance, etc away
    DFS will go deep down one path, and do that for every cell which will result in a time complexity of O((mn)^2)

    BFS starting at islands is not efficient
    by nature of BFS, doing BFS from all treasure cells will automatically give us the distance from the treasure one level at a time

approach:
    iterate thru grid, add all treasure cells to queue
    start bfs one level at a time
    while q:
        pop from q len(q) times
            search N, E, S W for each pop

O(ROWS*COLS) time
O(ROWS*COLS) space
"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
