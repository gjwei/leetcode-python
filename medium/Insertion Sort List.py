#coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head.next
        head.next= None
        while p:
            # print p.val
            t = p.next
            p.next = None
            #判断t的位置
            if p.val < head.val:
                p.next = head
                head = p
            else:
                q = head
                while q and q.next:
                    if q.val <= p.val < q.next.val:
                        #插入到q之后
                        p.next = q.next
                        q.next = p
                    q = q.next
                if p.next == None and p.val <= q.val:
                    p.next = q
            p = t
        return head
    
a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(1)
a.next.next.next = ListNode(3)

s = Solution()
t = s.insertionSortList(a)
print t.val
print t.next.val
print t.next.next.val
            
            




