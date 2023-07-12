# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
     def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head is None or head.next is None:
        #     return head
        # temp = head
        # head = head.next
        # temp.next, head.next = head.next, temp
        # # flag = 0
        # while temp is not None and temp.next is not None and temp.next.next is not None:
        #     node = temp.next
        #     temp.next = node.next
        #     node.next = temp.next.next
        #     temp.next.next = node
        #     if node.next is not None:
        #         temp = temp.next.next 
        #         # flag = 0
        #     if node.next == None:
        #         break
        #     flag = 1
        # return head
        
        if head is None or head.next is None:
            return head
        nodelist = head.next
        head.next = self.swapPairs(head.next)
        nodelist.next = head
        return nodelist
        
