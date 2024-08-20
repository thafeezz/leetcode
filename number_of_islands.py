"""
iterate thru elements in grid
if node is visited or 0, skip
if u find a 1, that is the root node
do bfs from that node
once bfs done (queue empty) thats 1 island

O(ROWS*COLS) time
O(ROWS*COLS) memory
"""


class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        queue = deque()
        visited = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        islands = 0
        
        # iterate thru elements in grid
            # if node is visited or 0, skip
        # if u find a 1, that is the root node
        # do bfs from that node
        # once bfs done (queue empty) thats 1 island

        def inBounds(tile) -> bool:
            if tile[0] < 0 or tile[0] >= ROWS or tile[1] < 0 or tile[1] >= COLS:
                return False
            return True

        def isVisited(tile) -> bool:
            return tile in visited

        def getTile(tile) -> string:
            return grid[tile[0]][tile[1]]

        for r in range(ROWS):
            for c in range(COLS):
                curr = (r, c)
                if curr in visited or grid[curr[0]][curr[1]] == "0":
                    continue

                queue.append(curr)
                visited.add(curr)
                
                # BFS
                while queue:
                    tile = queue.popleft()

                    north = (tile[0]-1, tile[1])
                    east = (tile[0], tile[1]+1)
                    south = (tile[0]+1, tile[1])
                    west = (tile[0], tile[1]-1)

                    if inBounds(north) and getTile(north) == "1" and not isVisited(north):
                        queue.append(north)
                        visited.add(north)
                    if inBounds(east) and getTile(east) == "1" and not isVisited(east):
                        queue.append(east)
                        visited.add(east)
                    if inBounds(south) and getTile(south) == "1" and not isVisited(south):
                        queue.append(south)
                        visited.add(south)
                    if inBounds(west) and getTile(west) == "1" and not isVisited(west):
                        queue.append(west)
                        visited.add(west)

                islands += 1

        return islands