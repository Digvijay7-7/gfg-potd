'''
You are given a string s. You need to reverse the string.
Example 1:
Input:
s = Geeks
Output: skeeG

Example 2:
Input:
s = for
Output: rof

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
'''

#User function Template for python3

class Solution:
    def reverseWord(self, s):
        s = s[::-1]
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        ob = Solution()
        print(ob.reverseWord(s))
        t = t-1

# } Driver Code Ends