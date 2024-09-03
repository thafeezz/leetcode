"""
build adj list using hashmap, perform dfs traversal on map


O(n+p) time, where n is numCourses (nodes) and p is prerequisites (edges)
O(n+p) memory
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if there is a cycle, return false
        visited = set()
        prereq_map = {i: [] for i in range(numCourses)} # adj list

        for course_a, course_b in prerequisites:
            prereq_map[course_a].append(course_b)

        def dfs(course):
            if course in visited:
                return False

            prereqs = prereq_map[course]
            if not prereqs:
                return True

            visited.add(course)
            for pr in prereqs:
                if not dfs(pr): return False

            """
            consider the same case below, that case is not a cycle, but had we not removed 1 from visited after traversing its path
            traversing from 2->1 would have said there is a cycle even tho there isnt, just because we had traversed 1's path already
            """
            visited.remove(course)

            """
            this is an optimization, in the case where a class has a prereq that has already been searched for a cycle,
            we set the prereq list to empty, signifying that it has been cleared for not having a cycle
            consider this case:
            [[0,1],[0,2],[1,3],[1,4],[3,4],[2,1]]

            since course 2 links to course 1, and course 1 is processed first, if we didnt set course 1's list to [],
            we would have to traverse it all the way back down to course 4 to see that the courses are possible to take
            """
            prereq_map[course] = [] 

            return True
        
        """
        we iterate over all courses in the case that the graphs are not connected
        consider this case:
        [[0,1], [2,3]]

        this is a valid input and should return True, but if we dfs starting at 0, we wont validate the graph from 2->3
        """
        for course in range(numCourses):
            if not dfs(course): return False

        return True
