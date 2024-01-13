# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = set()
        self.traverse(root, 0)

    # 給定 root 和 root value，還原二叉樹，並記錄到 nodes 中
    def traverse(self, root, val):
        if root is None: return
        
        root.val = val
        self.nodes.add(root.val)
        if root.left:
            self.traverse(root.left, 2 * val + 1)
        if root.right:
            self.traverse(root.right, 2 * val + 2)


    def find(self, target: int) -> bool:
        return target in self.nodes


from collections import defaultdict
class FindElements2:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = defaultdict(bool)
        self.traverse(root, 0)

    # 給定 root 和 root value，還原二叉樹，並記錄到 nodes 中
    def traverse(self, root, val):
        if root is None: return
        
        root.val = val
        self.nodes[root.val] = True
        if root.left:
            self.traverse(root.left, 2 * val + 1)
        if root.right:
            self.traverse(root.right, 2 * val + 2)


    def find(self, target: int) -> bool:
        return self.nodes[target]