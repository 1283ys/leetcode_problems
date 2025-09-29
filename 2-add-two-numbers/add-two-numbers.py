# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head= ListNode(0)
        current= head
        carry=0
        while l1 != None or l2 != None or carry !=0:
            if l1 != None :
                l1value = l1.val
            else :
                l1value=0        
            
            if l2 != None :
                l2value = l2.val
            else :
                l2value=0
            Sum = l1value + l2value + carry
            carry=Sum //10
            node= ListNode(Sum % 10)
            current.next =node
            current= node
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return head.next        
        
        