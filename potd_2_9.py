'''
Given a binary tree and a budget. Assume you are at the root of the tree(level 1), you need to maximise the count of leaf nodes you can visit in your budget if the cost of visiting a leaf node is equal to the level of that leaf node.

Example 1:

Input: 
                  10
                /    \
               8      2
             /      /   \
            3      3     6
                    \
                     4
and budget = 8
Output: 2
Explanation:
Cost For visiting Leaf Node 3: 3
Cost For visiting Leaf Node 4: 4
Cost For visiting Leaf Node 6: 3
In budget 8 one can visit Max 2 Leaf Nodes.
Example 2:

Input: 
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
and budget = 5
Output: 1
Explanation: We can only visit either node 4 or 5.
Your Task:

You don't need to read input or print anything. Your task is to complete the function getCount() which takes root node of the tree and a integer denoting the budget as input parameters and returns an integer denoting the count of visited leaf nodes of the tree.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
'''

#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

from collections import defaultdict

class Solution:
    def t(self,root,level,lpl):
        if root.left is None and root.right is None:
            lpl[level] += 1
        if root.left is not None:
            self.t(root.left, level+1, lpl)
        if root.right is not None:
            self.t(root.right, level+1, lpl)
            
    def getCount(self,root,n):
        lpl = defaultdict(lambda: 0)
        self.t(root, 1, lpl)
        
        count = 0
        for key in sorted(lpl.keys()):
            val = lpl[key]
            if key*val <= n:
                count += val
                n -= key*val
            else:
                count += (n // key)
                break
        
        return count
        
        
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
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
def inord(root):
    if not root:
        return
    inord(root.left)
    print(root.data,end=' ')
    inord(root.right)
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s=input()
        k = int(input());
        root=buildTree(s)
        ob = Solution()
        res = ob.getCount(root,k)
        print(res)