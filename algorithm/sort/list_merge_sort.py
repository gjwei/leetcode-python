class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def list_merge_sort(a):
    if not a:
        return None
    if a and not a.next:
        return a
    if a and a.next and not a.next.next:
        a.val, a.next.val = min(a.val, a.next.val), max(a.val, a.next.val)
        return a
    left_head, right_head = get_mid_list(a)
    left = list_merge_sort(left_head)
    right = list_merge_sort(right_head)
    return merge(left, right)


def merge(left, right):
    head = p = ListNode(-2<<30)
    while left or right:
        if (left and right and left.val < right.val) or (left and not right):
            p.next = left
            left = left.next
        else:
            p.next = right
            right = right.next
        p = p.next
        p.next = None
    return head.next



def get_mid_list(head):
    if not head:
        return None
    slow, fast = head, head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    left = head
    right = slow.next
    slow.next = None
    return left, right
    
