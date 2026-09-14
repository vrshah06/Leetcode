class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def postorderTraversal(root):
    postorder = []
    if root is None:
        return postorder
    stack1 = []
    stack2 = []
    #Push the root node to the first stack
    stack1.append(root)
    #Iterate traversal to populate the second stack
    while stack1:
        root = stack1.pop()
        stack2.append(root)
        #Push the left and right children of the popped node to the first stack
        if root.left:
            stack1.append(root.left)
        if root.right:
            stack1.append(root.right)
    #Populate the postorder list by popping all elements from the second stack
    while stack2:
        root = stack2.pop()
        postorder.append(root.val)
    return postorder
if __name__ == "__main__":
    # Example usage:
    # Constructing a binary tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = postorderTraversal(root)
    print(result)  # Output: [4, 5, 2, 3, 1]



#Other method
# Tree node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution class with postorder function
class Solution:
    def postorderTraversal(self, root, result):
        # Base case: if node is None
        if not root:
            return
        
        # Traverse left subtree
        self.postorderTraversal(root.left, result)
        
        # Traverse right subtree
        self.postorderTraversal(root.right, result)
        
        # Add current node value
        result.append(root.val)

# Main function
if __name__ == "__main__":
    # Build tree:    1
    #              /   \
    #             2     3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    # Object of solution
    sol = Solution()
    result = []

    # Call postorder traversal
    sol.postorderTraversal(root, result)

    # Print result
    print(*result)
