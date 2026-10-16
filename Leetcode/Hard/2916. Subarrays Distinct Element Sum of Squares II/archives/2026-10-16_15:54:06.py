from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1

        s = [0] * (2 * size)
        q = [0] * (2 * size)
        lazy = [0] * size
        length = [0] * (2 * size)

        for i in range(n):
            length[size + i] = 1
        for i in range(size - 1, 0, -1):
            length[i] = length[i * 2] + length[i * 2 + 1]

        def apply(k, v):
            old = s[k]
            q[k] = (q[k] + 2 * v * old + length[k] * v * v) % MOD
            s[k] = (old + length[k] * v) % MOD
            if k < size:
                lazy[k] = (lazy[k] + v) % MOD

        def push(k):
            if lazy[k]:
                v = lazy[k]
                apply(k * 2, v)
                apply(k * 2 + 1, v)
                lazy[k] = 0

        last = {}
        ans = 0
        height = size.bit_length() - 1

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1
            l = left + size
            r = i + size
            l0, r0 = l, r

            for h in range(height, 0, -1):
                if ((l0 >> h) << h) != l0:
                    push(l0 >> h)
                if (((r0 + 1) >> h) << h) != r0 + 1:
                    push(r0 >> h)

            while l <= r:
                if l & 1:
                    apply(l, 1)
                    l += 1
                if not (r & 1):
                    apply(r, 1)
                    r -= 1
                l >>= 1
                r >>= 1

            for h in range(1, height + 1):
                if ((l0 >> h) << h) != l0:
                    k = l0 >> h
                    s[k] = (s[k * 2] + s[k * 2 + 1]) % MOD
                    q[k] = (q[k * 2] + q[k * 2 + 1]) % MOD
                if (((r0 + 1) >> h) << h) != r0 + 1:
                    k = r0 >> h
                    s[k] = (s[k * 2] + s[k * 2 + 1]) % MOD
                    q[k] = (q[k * 2] + q[k * 2 + 1]) % MOD

            last[x] = i
            ans = (ans + q[1]) % MOD

        return ans