"""
iterate thru elements in grid
if node is visited or 0, skip
if u find a 1, that is the root node
do bfs from that node
once bfs done (queue empty) thats 1 island, count area and tax max


O(ROWS*COLS) time
O(ROWS*COLS) memory
"""

# bfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        queue = deque()
        max_island_area = 0

        ROWS, COLS = len(grid), len(grid[0])

        def getTile(tile):
            return grid[tile[0]][tile[1]]

        def inBounds(tile):
            if tile[0] < 0 or tile[0] >= ROWS or tile[1] < 0 or tile[1] >= COLS:
                return False
            return True

        def isVisited(tile):
            return tile in visited

        for r in range(ROWS):
            for c in range(COLS):
                curr_tile = (r, c)

                if getTile(curr_tile) == 0 or curr_tile in visited:
                    continue

                # scope islandArea per bfs
                queue.append(curr_tile)
                visited.add(curr_tile)
                island_area = 1

                # bfs
                while queue:
                    tile = queue.popleft()
                    print(tile)

                    # N, E, S, W
                    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    for dir in directions:
                        new_dir = (tile[0] + dir[0], tile[1] + dir[1])
                        if inBounds(new_dir) and getTile(new_dir) == 1 and not isVisited(new_dir):
                            queue.append(new_dir)
                            visited.add(new_dir)
                            island_area += 1
                
                max_island_area = max(island_area, max_island_area)

        return max_island_area

# recursive dfs (neetcode sol)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
