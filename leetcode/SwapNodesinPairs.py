# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        node = start
        if(start.next == None):
            return None
        elif(head.next == None):
            return start.next
        else:
            while(node!=None and node.next!=None and node.next.next!=None):
                print node.val
                temp = node.next
                node.next = temp.next
                temp.next = node.next.next
                node.next.next = temp
                node = node.next.next
            return start.next


def printL(head):
    while(head!=None):
        print head.val,
        head = head.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    printL(head)
    s = Solution()
    printL(s.swapPairs(head))
