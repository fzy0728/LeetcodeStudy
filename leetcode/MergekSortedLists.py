class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if(len(lists)==1):
            return lists(0)
        for i in range(len(lists)-1):
            lists[i + 1] = self.mergeTwoLists(lists[i],lists[i+1])
        return lists[len(lists)-1]



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