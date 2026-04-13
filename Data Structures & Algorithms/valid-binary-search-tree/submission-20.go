/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isValidBST(root *TreeNode) bool {
    return Res(root, -1001, 1001)
}

func Res(root *TreeNode, min int, max int) bool{
    if root == nil{
        return true
    }
    if root.Val <= min || root.Val >= max{
            return false
    }
    return Res(root.Left, min, root.Val) && Res(root.Right, root.Val, max)
}
