# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printL(head):
    while(head!=None):
        print head.val,
        head = head.next
    print ''
class Solution(object):

    def confire(self, head, k):
        if (head == None):
            return False
        while (k > 0):
            if (head== None):
                return False
            head = head.next
            k = k - 1
        return True

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        node = head
        em = None
        if (head == None):
            return None
        elif (head.next == None):
            return head
        else:
            if(self.confire(node,k)):
                st, em, node = self.reverse(node, k)
                start.next = st
            while(self.confire(node,k)):
                s,e,node = self.reverse(node,k)
                em.next = s
                em = e
            if(em!=None):
                em.next = node
        return start.next

    def reverse(self,head,k):
        start = ListNode(0)
        start.next = head
        while(head.next!=None and k-1>0 ):
            temp = head.next
            head.next = temp.next
            temp.next = start.next
            start.next = temp
            k-=1
        l = head.next
        return start.next,head,l


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)

    s = Solution()

    printL(s.reverseKGroup(head,7))

    # printL(s.reverse(head,2))

