/**
 * Definition for a binary tree node.
*/
class TreeNode {
val: number
     left: TreeNode | null
     right: TreeNode | null
     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.left = (left===undefined ? null : left)
         this.right = (right===undefined ? null : right)
     }
 }

function levelOrder(root: TreeNode | null): number[][] {
    var res: number[][] = new Array()

    if (Object.is(root, null)) return res

    var q: TreeNode[] = new Array()
    q.push(root!)

    while (q.length !== 0) {
        var level: number[] = new Array()
        var s = q.length
        for (let i = 0; i < s; i++) {
            var node: TreeNode = q.shift()!
            level.push(node.val)
            if (node.left) q.push(node.left)
            if (node.right) q.push(node.right)
        }

        res.push(level)
    }

    return res
};