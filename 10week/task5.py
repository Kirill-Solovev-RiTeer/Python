"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree
"""
def fun(A,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    root=TreeNode(A[mid].val)
    root.left=fun(A,start,mid-1)
    root.right=fun(A,mid+1,end)
    return root

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums=[]
        temp=head
        while temp!=None:
            nums.append(temp)
            temp=temp.next
        return fun(nums,0,len(nums)-1)