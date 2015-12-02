# Definition for singly-linked list.
import heapq
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class warper:
    def __init__(self,x):
        self.node=x[0];
        self.index=x[1];

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap=[];
        result=[];
        for i in range(len(lists)):
            if( lists[i]):
                heapq.heappush(heap,(lists[i][0],i));
                lists[i].popleft();
        temp=heapq.heappop(heap);
        while(temp):
            result.append(temp[0]);
            if(lists[i]):
                heapq.heappush(headp,(lists[i][0],i);
        return result;

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node: 
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0); curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next: 
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next
        