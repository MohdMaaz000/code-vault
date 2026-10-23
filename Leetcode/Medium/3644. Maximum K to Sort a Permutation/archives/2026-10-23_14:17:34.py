class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1

        for i, x in enumerate(nums):
            if x != i:
                ans &= x

        return max(ans, 0)