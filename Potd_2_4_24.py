'''
Given a binary search tree having n (n>1) nodes, the task is to find the minimum absolute difference between any two nodes.

Example 1:
Input:
Input tree: https://prnt.sc/Bjl1MAc6tDXT
Output:
10
Explanation:
There are no two nodes whose absolute difference is smaller than 10.

Example 2:
Input:
Input tree: https://prnt.sc/LFmmN-w-tami
Output:
20
Explanation:
There are no two nodes whose absolute difference is smaller than 20.

Your Task:
You don't have to take any input. Just complete the function absolute_diff() , that takes root as input and return minimum absolute difference between any two nodes.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(Height of tree)
'''
# class Node:
#     def __init__(self):
#         self.data = None
#         self.left = None
#         self.right = None
        
class Solution:
    def inorderTraversal(self, root):
        stack = []
        inorder = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorder.append(root.data)
            root = root.right
        return inorder
    
    def absolute_diff(self, root):
        # Perform inorder traversal to get sorted elements.
        inorder = self.inorderTraversal(root)
        
        min_diff = float('inf')
        for i in range(1, len(inorder)):
            diff = abs(inorder[i] - inorder[i - 1])
            min_diff = min(min_diff, diff)
        
        return min_diff



#{ 
 # Driver Code Starts
from collections import deque


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to Build Tree
def buildTree(str):
    # Corner Case
    if len(str) == 0 or str[0] == 'N':
        return None

    # Creating list of strings from input string after splitting by space
    ip = str.split()

    # Create the root of the tree
    root = Node(int(ip[0]))

    # Push the root to the queue
    queue = deque()
    queue.append(root)

    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        currNode = queue.popleft()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            queue.append(currNode.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            queue.append(currNode.right)

        i += 1

    return root


for _ in range(int(input())):
    s = input()
    root = buildTree(s)
    if root is None:
        continue
    if root.left is None and root.right is None:
        continue

    ob = Solution()
    print(ob.absolute_diff(root))

# } Driver Code Ends