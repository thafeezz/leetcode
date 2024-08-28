"""
2 pass solution, take all tiles touching pacific ocean (top and left row), and all tiles touching atlantic (bottom and right row)
dfs from these tiles and add all tiles that satisfy constraint (tile u are adding must have higher elevation than current so water can flow)

one set contains all tiles that will allow water to flow into the pacific, the other is the same but with the atlantic instead
take the set intersection at the end of the two sets

O(ROWS*COLS) time
O(ROWS*COLS) space
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def inBounds(tile):
            return 0 <= tile[0] < ROWS and 0 <= tile[1] < COLS

        def getValue(tile):
            return heights[tile[0]][tile[1]]

        def dfs(tile, ocean_set):
            if tile in ocean_set:
                return
            
            ocean_set.add(tile)

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for d in directions:
                new_tile = (tile[0] + d[0], tile[1] + d[1])
                if inBounds(new_tile) and getValue(new_tile) >= getValue(tile):
                    dfs(new_tile, ocean_set)

        for r in range(ROWS):
            dfs((r, 0), pacific)
            dfs((r, COLS - 1), atlantic)

        for c in range(COLS):
            dfs((0, c), pacific)
            dfs((ROWS - 1, c), atlantic)

        result = list(pacific & atlantic)
        return result
