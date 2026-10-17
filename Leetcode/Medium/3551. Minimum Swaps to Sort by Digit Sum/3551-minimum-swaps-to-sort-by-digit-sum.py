from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        target = {v: i for i, v in enumerate(arr)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target[nums[i]] == i:
                continue

            j = i
            cycle = 0

            while not visited[j]:
                visited[j] = True
                j = target[nums[j]]
                cycle += 1

            swaps += cycle - 1

        return swaps