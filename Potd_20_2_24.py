'''
Given a string s and a dictionary of n words dictionary, find out if "s" can be segmented into a space-separated sequence of dictionary words.
Return 1 if it is possible to break the s into a sequence of dictionary words, else return 0. 

Note: From the dictionary dictionary each word can be taken any number of times and in any order.

Example 1:
Input:
n = 6
s = "ilike"
dictionary = { "i", "like", "sam", "sung", "samsung", "mobile"}
Output:
1
Explanation:
The string can be segmented as "i like".

Example 2:
Input:
n = 6
s = "ilikesamsung"
dictionary = { "i", "like", "sam", "sung", "samsung", "mobile"}
Output:
1
Explanation:
The string can be segmented as 
"i like samsung" or "i like sam sung".
Your Task:
Complete wordBreak() function which takes a string and list of strings as a parameter and returns 1 if it is possible to break words, else returns 0. You don't need to read any input or print any output, it is done by driver code.

Expected Time Complexity: O(len(s)^2)
Expected Space Complexity: O(len(s))

Constraints:
1 ≤ n ≤ 12
1 ≤ len(s) ≤ 1100
'''

#User function Template for python3

class Solution:
    def wordBreak(self, n, s, dictionary):
        # Complete this function
        dictionary=sorted(dictionary[::],key=lambda x:len(x))
        dictionary=dictionary[::-1]
        for i in dictionary:
            while i in s:
                s=s.replace(i,"")
        if s == "":
            return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends