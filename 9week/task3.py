"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/validate-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree
"""
class Solution:
    res=True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs (r,mx,mn):
            if r.right:
                if r.right.val<=r.val or r.right.val>=mx:
                    self.res =  False

                dfs(r.right,mx ,r.val)
            if r.left:
                if r.left.val>=r.val or r.left.val<=mn:
                    self.res=  False
                dfs(r.left,r.val,mn)

        dfs(root,2**31,-2**31-1)
        return self.res