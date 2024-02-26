'''
Given a string s of length n, find all the possible subsequences of the string s in lexicographically-sorted order.

Example 1:

Input : 
s = "abc"
Output: 
a ab abc ac b bc c
Explanation : 
There are a total 7 number of subsequences possible 
for the given string, and they are mentioned above 
in lexicographically sorted order.
Example 2:

Input: 
s = "aa"
Output: 
a a aa
Explanation : 
There are a total 3 number of subsequences possible 
for the given string, and they are mentioned above 
in lexicographically sorted order.
Your Task:
You don't need to read input or print anything. Your task is to complete the function AllPossibleStrings() which takes a string s as the input parameter and returns a list of all possible subsequences (non-empty) that can be formed from s in lexicographically-sorted order.

Expected Time Complexity: O( n*2^n  )
Expected Space Complexity: O( n * 2^n )
'''

#User function Template for python3
class Solution:
    def AllPossibleStrings(self, s):
        result = []
        
        # Recursive function to generate subsequences
        def generateSubsequences(curr, index):
            # Add the current subsequence to the result
            if curr:
                result.append(curr)
            
            # Iterate over remaining characters in the string
            for i in range(index, len(s)):
                # Include the current character and recurse
                generateSubsequences(curr + s[i], i + 1)
        
        # Generate subsequences starting from index 0
        generateSubsequences("", 0)
        
        # Sort the result lexicographically
        result.sort()
        
        return result
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends