"""
BFS level order traversal
add all rotten oranges to queue
iterate thru queue level by level and increment minutes
add adjacent cells

count number of rotten and normal oranges to see when an orange cannot be rotten

O(ROWS*COLS) time
O(ROWS*COLS) space
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        total_oranges = 0
        rotten_oranges = 0

        def inBounds(tile):
            if tile[0] < 0 or tile[0] >= ROWS or tile[1] < 0 or tile[1] >= COLS:
                return False
            return True

        def getTile(tile):
            return grid[tile[0]][tile[1]]

        def isVisited(tile):
            return tile in visited

        def addTile(tile):
            nonlocal rotten_oranges
            if inBounds(tile) and not isVisited(tile) and getTile(tile) == 1:
                queue.append(tile)
                visited.add(tile)
                rotten_oranges += 1

        for r in range(ROWS):
            for c in range(COLS):
                tile = (r,c)
                if getTile(tile) == 2:
                    queue.append(tile)
                    visited.add(tile)
                    rotten_oranges += 1
                    total_oranges += 1
                elif getTile(tile) == 1:
                    total_oranges += 1

        minutes = 0

        while queue:
            level_len = len(queue)
            for _ in range(level_len):
                tile = queue.popleft()

                north = (tile[0]-1, tile[1])
                east = (tile[0], tile[1]+1)
                south = (tile[0]+1, tile[1])
                west = (tile[0], tile[1]-1)
                
                addTile(north)
                addTile(east)
                addTile(south)
                addTile(west)

            if queue:
                minutes += 1

        return minutes if total_oranges == rotten_oranges else -1
