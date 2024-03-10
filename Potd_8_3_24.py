'''
Given a string s which contains only lower alphabetic characters, check if it is possible to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string. Return true if it is possible to do else return false.

Note: The driver code print 1 if the value returned is true, otherwise 0.

Example 1:
Input:
s = "xyyz"
Output: 
1 
Explanation: 
Removing one 'y' will make frequency of each character to be 1.

Example 2:
Input:
s = "xxxxyyzz"
Output: 
0
Explanation: 
Frequency can not be made same by removing at most one character.
Your Task:  
You dont need to read input or print anything. Complete the function sameFreq() which takes a string as input parameter and returns a boolean value denoting if same frequency is possible or not.

Expected Time Complexity: O(|s|) 
Expected Auxiliary Space: O(1)
'''

#User function Template for python3
class Solution:
    def sameFreq(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        values = list(freq.values())
        unique_values = set(values)

        if len(unique_values) == 1:
            return True
        
        if len(unique_values) == 2:
            # Check if one character has a frequency of 1
            if values.count(1) == 1:
                return True
            # Check if one character can be removed to make frequencies same
            for v in unique_values:
                if values.count(v) == 1 and (v - 1 in unique_values or v == 1):
                    return True
        
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends