'''
Given a binary tree with N nodes, in which each node value represents number of candies present at that node. In one move, one may choose two adjacent nodes and move only one candy from one node to another (the move may be from parent to child, or from child to parent.) 
The task is to find the number of moves required such that every node has exactly one candy.
Note that the testcases are framed such that it is always possible to achieve a configuration in which every node has exactly one candy, after some moves.

Example 1:
Input :      3
           /   \
          0     0 
Output : 2
Explanation: 
From the root of the tree, we move one 
candy to its left child, and one candy to
its right child.

Example 2:
Input :      0
           /   \
          3     0  
Output : 3
Explanation : 
From the left child of the root, we move 
two candies to the root [taking two moves]. 
Then, we move one candy from the root of the 
tree to the right child.
Your task :
You don't have to read input or print anything. Your task is to complete the function distributeCandy() which takes the root of the tree as input and returns the number of moves required such that every node has exactly one candy.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(height of the tree)
'''

#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def distributeCandy(self, root):
        def dfs(node=root):
            if not node:
                return 0,0,0
            l=dfs(node.left)
            r=dfs(node.right)
            res=abs(l[0]-l[1]+r[0]-r[1]+node.data-1)
            return l[0]+r[0]+node.data,l[1]+r[1]+1,res+l[2]+r[2]
        return dfs(root.left)[2]+dfs(root.right)[2]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s=input()
        root = buildTree(s)
        ob = Solution()
        print(ob.distributeCandy(root))
        
            
# } Driver Code Ends