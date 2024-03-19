'''
You are given a Linked list of size n. The list is in alternating ascending and descending orders. Sort the given linked list in non-decreasing order.

Example 1:
Input:
n = 6
LinkedList = 1->9->2->8->3->7
Output: 1 2 3 7 8 9
Explanation: 
After sorting the given list will be 1->2->3->7->8->9.

Example 2:
Input:
n = 5
LinkedList = 13->99->21->80->50
Output: 13 21 50 80 99
Explanation:
After sorting the given list will be 13->21->50->80->99.
Your Task:
You do not need to read input or print anything. The task is to complete the function sort() which should sort the linked list of size n in non-decreasing order. 

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
'''

#User function Template for python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def merge(self, h1, h2):
        dummy = Node(0)
        tail = dummy
        
        while h1 and h2:
            if h1.data < h2.data:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            tail = tail.next
        
        if h1:
            tail.next = h1
        if h2:
            tail.next = h2
        
        return dummy.next
    
    def split(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        
        return head, second_half
    
    def sort(self, head):
        if not head or not head.next:
            return head
        
        first_half, second_half = self.split(head)
        
        first_half = self.sort(first_half)
        second_half = self.sort(second_half)
        
        return self.merge(first_half, second_half)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        
def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):        
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
        
        ob = Solution()
        resHead=ob.sort(ll1.head)
        printList(resHead)
        print()
            
# } Driver Code Ends