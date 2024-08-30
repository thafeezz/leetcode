"""
find an O on the edge, perform dfs to find any Os connected to the edge O
turn any Os connected to the edge Os to a T (temp)

iterate thru entire board and change Xs to Os and Ts to Os
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find an O on the edge, perform dfs
        # turn any Os connected to the edge Os to a T (temp)
        # iterate thru entire board and change Xs to Os and Ts to Os

        def inBounds(tile):
            return 0 <= tile[0] < ROWS and 0 <= tile[1] < COLS

        def getTile(tile):
            return board[tile[0]][tile[1]]
        
        def setTile(tile, val):
            board[tile[0]][tile[1]] = val

        def dfs(tile):
            if tile in visited or not inBounds(tile) or getTile(tile) == 'X':
                return

            setTile(tile, 'T')
            visited.add(tile)

            n = (tile[0]-1,tile[1])
            e = (tile[0], tile[1]+1)
            s = (tile[0]+1, tile[1])
            w = (tile[0], tile[1]-1)

            dfs(n)
            dfs(e)
            dfs(s)
            dfs(w)

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        for r in range(ROWS):
            dfs((r,0))
            dfs((r,COLS-1))
            
        for c in range(COLS):
            dfs((0,c))
            dfs((ROWS-1,c))


        for r in range(ROWS):
            for c in range(COLS):
                tile = (r,c)
                if getTile(tile) == 'O':
                    setTile(tile, 'X')
                elif getTile(tile) == 'T':
                    setTile(tile, 'O')
                
    

