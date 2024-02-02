'''
Complete the Insert and Search functions for a Trie Data Structure. 

Insert: Accepts the Trie's root and a string, modifies the root in-place, and returns nothing.
Search: Takes the Trie's root and a string, returns true if the string is in the Trie, otherwise false.
Note: To test the correctness of your code, the code-judge will be inserting a list of N strings called into the Trie, and then will search for the string key in the Trie. The code-judge will generate 1 if the key is present in the Trie, else 0.

Example 1:
Input:
n = 8
list[] = {the, a, there, answer, any, by, bye, their}
key = the
Output: 1
Explanation: 
"the" is present in the given set of strings. 

Example 2:
Input:
n = 8
list[] = {the, a, there, answer, any, by, bye, their}
key = geeks
Output: 0
Explanation: 
"geeks" is not present in the
given set of strings.

Your Task:
You do not have to take any input or print anything. Complete insert and search functions. 

Expected Time Complexity: O(M+|key|)
Expected Auxiliary Space: O(M)
Here M = sum of the length of all strings which are present in the list[] 

Constraints:
1 <= N <= 10^4
1 <= length of list[i] <= 30
All strings will constitute of lowercase alphabets only.
'''

"""
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""

class Solution:
    # Function to insert a string into the Trie.
    def insert(self, root, key):
        # Start at the root of the Trie.
        node = root
        # Traverse through each character in the key.
        for char in key:
            # Calculate the index of the current character in the children array.
            index = ord(char) - ord('a')
            # If the child node does not exist, create a new TrieNode.
            if not node.children[index]:
                node.children[index] = TrieNode()
            # Move to the child node.
            node = node.children[index]
        # Mark the last node as the end of the inserted word.
        node.isEndOfWord = True
    
    # Function to search for a string in the Trie.
    def search(self, root, key):
        # Start at the root of the Trie.
        node = root
        # Traverse through each character in the key.
        for char in key:
            # Calculate the index of the current character in the children array.
            index = ord(char) - ord('a')
            # If the child node does not exist, the key is not present in the Trie.
            if not node.children[index]:
                return False
            # Move to the child node.
            node = node.children[index]
        # Check if the last node marks the end of a word.
        return node.isEndOfWord

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        ob = Solution()
        
        for s in arr:
            ob.insert(t.root,s)
        
        if ob.search(t.root,strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends