# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 給定 root 為根節點的 BST，返回刪除 key 節點後的BST
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None: return None

        if root.val == key:
            # 情況 1: root 為葉子節點
            # 情況 2: root 為根節點且有 1 個子節點(左or右)
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # 情況 3: root 為根節點且有 2 個子節點(左and右)
            new_root = self.getMin(root.right)
            root.right = self.deleteNode(root.right, new_root.val)
            new_root.left = root.left
            new_root.right = root.right
            root = new_root

        elif root.val > key:
            # 去左側子樹刪除完 key 後，將返回的 BST 接回 root.left
            root.left = self.deleteNode(root.left, key)
        else: # root.val < key
            # 去右側子樹刪除完 key 後，將返回的 BST 接回 root.right
            root.right = self.deleteNode(root.right, key)
        return root
           
    # 獲取 node 為根節點的 BST 的最小值，返回該 node
    def getMin(self, node):
        while node.left:
            node = node.left
        return node

    # 獲取 node 為根節點的 BST 的最大值，返回該 node
    def getMax(self, node):
        while node.right:
            node = node.right
        return node