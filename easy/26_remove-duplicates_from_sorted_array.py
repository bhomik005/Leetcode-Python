class Solution:
    # arr = [1, 2, 3, 4, 3, 4, 4] - sorted in non decreasing order
    # arr =           L        R
    # res = [1, 2, 3, 4, _, _ ,_], k = 4
    # two pointer approach 
    # O(n) time | O(1) space
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        while right < len(nums):
            if nums[left] != nums[right]:
                nums[left + 1] = nums[right]
                left += 1
            right += 1   
        return left + 1
