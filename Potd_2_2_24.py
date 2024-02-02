'''
Given a string, s, the objective is to convert it into integer format without utilizing any built-in functions. If the conversion is not feasible, the function should return -1.

Note: Conversion is feasible only if all characters in the string are numeric or if its first character is '-' and rest are numeric.

Example 1:
Input:
s = "-123"
Output: 
-123
Explanation:
It is possible to convert -123 into an integer 
and is so returned in the form of an integer

Example 2:
Input:
s = "21a"
Output: 
-1
Explanation: 
The output is -1 as, due to the inclusion of 'a',
the given string cannot be converted to an integer.
Your Task:
You do not have to take any input or print anything. Complete the function atoi() which takes a string s as an input parameter and returns an integer value representing the given string. If the conversion is not feasible, the function should return -1.

|s| = length of string str.
Expected Time Complexity: O( |s| ), 
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |s| ≤ 10
'''

#User function template for Python

class Solution:
    def atoi(self, s):
        # Check if the string is empty
        if not s:
            return -1

        # Initialize result and sign variables
        result = 0
        sign = 1

        # Initialize index to iterate through the string
        i = 0

        # Skip leading whitespaces
        while i < len(s) and s[i] == ' ':
            i += 1

        # Check for optional sign
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Iterate through the remaining characters
        while i < len(s) and s[i].isdigit():
            # Check for overflow
            if result > (2 ** 31 - 1) // 10 or (result == (2 ** 31 - 1) // 10 and int(s[i]) > 7):
                return -1 if sign == 1 else -2 ** 31

            # Update result
            result = result * 10 + int(s[i])
            i += 1

        # Check for additional non-numeric characters
        while i < len(s) and not s[i].isspace():
            return -1

        # Apply sign to the result
        return result * sign


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends