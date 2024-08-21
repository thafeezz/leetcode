"""
dfs on input graph
use hashmap to map old nodes to copied nodes
base case:
    if old node already copied, return new node
    this basically draws an edge between the two nodes

add to map once copy has been created
return copy


O(V+E ) time
O(2V+E) = O(V+E) memory
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        created = {}
        
        def dfs(node):
            if node in created:
                return created[node]

            cp = Node(node.val, [])

            created[node] = cp

            for n in node.neighbors:
                neighbor_cp = dfs(n)
                cp.neighbors.append(neighbor_cp)

            return cp

        dfs(node)
        return created[node]
