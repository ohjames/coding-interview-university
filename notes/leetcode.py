# 191 Optimize


# 83
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if current is None:
            return
        while current.next:
            if current.val == current.next.val:
                new = current.next.next
                current.next = None
                current.next = new
            else:
                current = current.next
        return head

# 206 Recursion implementation
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            self.next = current.next
            current.next = prev
            prev = current
            current = self.next
        head = prev
        return head

# 1 Optimize
    def twoSum(self, nums: List[int], target:int) -> List[int]: 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []