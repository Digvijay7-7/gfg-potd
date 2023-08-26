/*
Given a string you need to print the size of the longest possible substring that has exactly K unique characters. If there is no possible substring then print -1.

Example 1:
Input:
S = "aabacbebebe", K = 3
Output: 
7
Explanation: 
"cbebebe" is the longest substring with 3 distinct characters.

Example 2:
Input: 
S = "aaaa", K = 2
Output: -1
Explanation: 
There's no substring with 2 distinct characters.

Your Task:
You don't need to read input or print anything. Your task is to complete the function longestKSubstr() which takes the string S and an integer K as input and returns the length of the longest substring with exactly K distinct characters. If there is no substring with exactly K distinct characters then return -1.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).

Constraints:
1 ≤ |S| ≤ 105
1 ≤ K ≤ 26
All characters are lowercase latin characters.
 */

import java.util.*;

class potd_26_8 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            String s = sc.next();
            int k = sc.nextInt();
            Solution obj = new Solution();
            System.out.println(obj.longestkSubstr(s, k));
            sc.close();
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    public int longestkSubstr(String s, int k) {
        int op = -1;
        int i=0,j=0;

        HashMap<Character,Integer> map = new HashMap<>();

        while(j<s.length()){
            char ch = s.charAt(j);
            map.put(ch,map.getOrDefault(ch,0)+1);
            if(map.size()==k) op = Math.max(op,j-i+1);

            while(map.size()>k){
                char a = s.charAt(i);
                map.put(a,map.get(a)-1);
                if(map.get(a)==0){
                    map.remove(a);
                }
                i++;
            }
            j++;
        }
        return op;
    }
}