class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        # O(n) time | O(1) space
        # two pointer approach
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k = k + 1
        return k
        
