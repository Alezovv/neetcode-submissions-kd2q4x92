/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isValidBST(root *TreeNode) bool {
    /* if root == nil{
        return true
    }
    if root.Left == nil && root.Right == nil{
        return true
    }

    val := root.Val
    if Compare(root, root.Left, root.Right) == true{
        if root.Left != nil{
            if root.Left.Val > val{
                return false
            }
        }
        if root.Right != nil{
            if root.Right.Val < val{
                return false
            }
        }
        return isValidBST(root.Left) && isValidBST(root.Right)

    }

    return false */
    return Res(root, -1001, 1001)

}

func Res(root *TreeNode, min int, max int) bool{
    if root == nil{
        return true
    }
    // if root.Left == nil && root.Right == nil{
    //     return true
    // }
    //VAL < MAX AND VAL > MIN
    /* if Compare(root, root.Left, root.Right) == true{ */
        if root.Val <= min || root.Val >= max{
                return false
            }
        
        // if root != nil{
        //     if root.Right.Val < max && root.Right.Val > min{
        //         return false
        //     }
        // }
        return Res(root.Left, min, root.Val) && Res(root.Right, root.Val, max)
    /* } */
    
}


/* func Compare(root *TreeNode, l *TreeNode, r *TreeNode) bool {
    if l == nil && r == nil{
        return true
    }
    if l == nil{
        return r.Val > root.Val
    }
    if r == nil{
        return l.Val < root.Val
    }

    return l.Val < root.Val && r.Val > root.Val
} */
