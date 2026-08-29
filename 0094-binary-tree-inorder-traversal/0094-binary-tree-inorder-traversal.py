class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        st = []
        cur = root
        
        while cur or st:
            while cur:
                st.append(cur)
                cur = cur.left
                
            cur = st.pop()
            res.append(cur.val)
            
            cur = cur.right
            
        return res