# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def gcd(x,y):
    x,y = max(x,y), min(x,y)
    if x%y == 0:
        return y 
    return gcd(y, x%y)

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curNode = head
        while curNode.next is not None:

            nextNode = curNode.next 

            gcd_val = gcd(curNode.val, nextNode.val)

            new_node = ListNode(gcd_val, nextNode) 
            curNode.next = new_node 

            curNode = new_node.next 
        return head 
            

        