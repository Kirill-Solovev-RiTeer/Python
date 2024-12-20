"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/unique-binary-search-trees-ii/description/?envType=problem-list-v2&envId=binary-tree
"""
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache
        def dfs(start,end):
            if start>end:
                return [None]

            ans=[]
            for i in range(start,end+1):
                left=dfs(start,i-1)
                right=dfs(i+1,end)
                for l in left:
                    for r in right:
                        root=TreeNode(i)
                        root.left=l
                        root.right=r
                        ans.append(root)
            return ans

        return dfs(1,n)   