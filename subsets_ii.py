"""
same as subsets i, this time skip duplicates, and sort nums array at start
after popping (backtracking step), increment index until you are not at a duplicate number, then continue

or use a set and check if sublist u are appending is in the answer set already (slow)

O(2^n + nlogn) time
O(n * 2^n) memory
"""

class Solution:
    ans = []
    sublist = []

    nums.sort()

    def dfs(i):
        if i >= len(nums):
            ans.append(sublist.copy())
            return

        sublist.append(nums[i])
        dfs(i+1)

        sublist.pop()

        while i + 1 < len(nums) and nums[i+1] == nums[i]:
            i += 1

        dfs(i+1)

    dfs(0)
    return ans

    # ans = set()
    # sublist = []

    # def dfs(i):
    #     if i >= len(nums):
    #         if set(tuple(sorted(sublist))) not in ans:
    #             ans.add(tuple(sorted(sublist.copy())))
    #         return

    #     sublist.append(nums[i])
    #     dfs(i+1)

    #     sublist.pop()
    #     dfs(i+1)

    # dfs(0)
    # return list(ans)
