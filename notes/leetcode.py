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

# 27
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

# 232 Implement queue such that each operation is amortized O(1) time?
        # Performing n operations will take O(n) time even if one of those operations may take longer
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()
        self.stack1.append(x)
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
    
    def pop(self) -> int:
        if len(self.stack1) == 0:
            return "Queue is empty"
        x = self.stack1[-1]
        self.stack1.pop()
        return x

    def peek(self) -> int:
        if len(self.stack1) == 0:
            return "Queue is empty"
        x = self.stack1[-1]
        return x

    def empty(self) -> bool:
        return len(self.stack1) == 0