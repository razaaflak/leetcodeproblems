class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum = self.ListToInt(l1) + self.ListToInt(l2)
        if sum < 10:
            return ListNode(val=sum)
        arr = [int(x) for x in str(sum)]
        res = ListNode()
        res.val = arr.pop()
        res.next = ListNode()
        curr = res.next
        while len(arr) > 0:
            curr.val = arr.pop()
            if len(arr) > 0 :
                curr.next = ListNode()
                curr = curr.next
        return res
        

    def ListToInt(self,l,pos=0):
        if l.next is None:
            return l.val * (10**pos)
        else:
            return l.val * (10**pos) + self.ListToInt(l.next,pos=pos+1)
        
