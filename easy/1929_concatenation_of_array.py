class Solution:
    # nums = [1, 2, 1] O(n) where n is the number of elements in the array
    # ans =  [1, 2, _, 1, 2, _] -> O(2 * n) -> O(n) space
    # clarifying question could be:
    # 1. How big the input array could be?
    #   
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        # O(n) time | O(2 * n) space
        for i in range(len(nums)):
            ans[i], ans[len(nums) + i] = nums[i], nums[i]
        return ans