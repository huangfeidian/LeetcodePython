# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dumb_head=ListNode(0);
        fake_head=dumb_head;
        fake_head.next=head;
        i=n;
        fake_end=fake_head.next;
        while(i>0):
            fake_end=fake_end.next;
            i-=1;
        while(fake_end):
            fake_head=fake_head.next;
            fake_end=fake_end.next;
        fake_head.next=fake_head.next.next;
        return dumb_head.next;