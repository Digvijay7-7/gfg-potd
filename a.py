'''
A critical connection refers to an edge that, upon removal, will make it impossible for certain nodes to reach each other through any path. You are given an undirected connected graph with v vertices and e edges and each vertex distinct and ranges from 0 to v-1, and you have to find all critical connections in the graph. It is ensured that there is at least one such edge present.

Note: The answers may be presented in various potential orders. Each edge should be displayed in sorted order. For instance, if there's an edge between node 1 and node 2, it should be stored as (1,2) rather than (2,1). Additionally, it is expected that you store the edges in sorted order.

Example 1:
Input:
https://prnt.sc/MtUgGwIJd_GU
Output:
0 1
0 2
Explanation: 
On removing edge (0, 1), you will not be able to
reach node 0 and 2 from node 1. Also, on removing
edge (0, 2), you will not be able to reach node 0
and 1 from node 2.

Example 2:
Input:
https://prnt.sc/Gd9l9MOtyc_Z
Output:
2 3
Explanation:
The edge between nodes 2 and 3 is the only
Critical connection in the given graph.
Your task:
You dont need to read input or print anything. Your task is to complete the function criticalConnections() which takes the integer v denoting the number of vertices and an adjacency list adj as input parameters and returns  a list of lists containing the Critical connections in the sorted order.

Expected Time Complexity: O(v + e)
Expected Auxiliary Space: O(v)

Constraints:
1 ≤ v, e ≤ 10^4
'''

#User function Template for python3

class Solution:
    def criticalConnections(self, V, adj):
        disc = [-1 for i in range(V)]
        low = [-1 for i in range(V)]
        self.time = 0
        bridges = []
        def SCC(u, par = -1):
            disc[u] = self.time
            low[u] = self.time
            self.time += 1
            for v in adj[u]:
                if v == par:
                    continue
                if disc[v] == -1:
                    SCC(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        if v > u:
                            bridges.append([u, v])
                        else:
                            bridges.append([v, u])
                else:
                    low[u] = min(low[u], disc[v])
        for i in range(V):
            if disc[i] == -1:
                SCC(i)
        bridges.sort()
        return bridges


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.criticalConnections(V, adj)
		for i in range(len(ans)):
		    print(ans[i][0],ans[i][1])

# } Driver Code Ends