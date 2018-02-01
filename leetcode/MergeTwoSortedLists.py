# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = ListNode(0)
        second = ListNode(0)
        first.next = l1
        templ1 = first
        second.next = l2

        if(l1 == None):
            return l2
        if(l2 == None):
            return l1
        while(l1!=None):
            if(l2==None):break
            if(l2.val >= l1.val):
                templ1 = l1
                l1 = l1.next
            else:
                templ2 = l2
                l2 = l2.next
                templ2.next = l1
                templ1.next = templ2
                templ1 = templ2
        if(l2!=None):
            templ1.next = l2
        return first.next

def Print(l):
    while(l!=None):
        print l.val,
        l = l.next

if __name__== '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(5)
    head1.next.next.next = ListNode(6)

    head2 = ListNode(3)
    head2.next = ListNode(4)


    s = Solution()
    Print(head1)
    print '\n'
    Print(head2)
    print '\n'
    Print(s.mergeTwoLists(head1,head2))

    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(4)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    s = Solution()
    print ''
    Print(head1)
    print '\n'
    Print(head2)
    print '\n'
    Print(s.mergeTwoLists(head1, head2))

    head1 = ListNode(2)

    head2 = ListNode(1)

    s = Solution()
    print ''
    Print(head1)
    print '\n'
    Print(head2)
    print '\n'
    Print(s.mergeTwoLists(head1, head2))