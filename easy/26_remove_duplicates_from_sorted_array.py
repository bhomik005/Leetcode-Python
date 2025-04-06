class Solution:
    # O(n) time | O(1) space (since we are modifying the array in place)
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        # if nums[k] != nums[i], then nums[k + 1] = nums[i], and i++ and k++
        for i in range(len(nums)):
            if nums[k] != nums[i]:
                nums[k + 1] = nums[i]
                k = k + 1
        return k + 1
