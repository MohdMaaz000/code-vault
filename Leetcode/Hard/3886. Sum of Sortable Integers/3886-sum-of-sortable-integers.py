class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)

        def is_rotation(a, b):
            k = len(a)

            # KMP prefix function for b
            pi = [0] * k
            j = 0
            for i in range(1, k):
                while j and b[i] != b[j]:
                    j = pi[j - 1]
                if b[i] == b[j]:
                    j += 1
                pi[i] = j

            # Search b in a + a, without building a + a
            j = 0
            for i in range(2 * k - 1):
                x = a[i % k]
                while j and x != b[j]:
                    j = pi[j - 1]
                if x == b[j]:
                    j += 1
                if j == k:
                    return True
            return False

        ans = 0

        # Enumerate divisors in O(sqrt(n))
        divisors = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
            d += 1

        for k in divisors:
            valid = True

            for start in range(0, n, k):
                a = nums[start:start + k]
                b = target[start:start + k]

                if not is_rotation(a, b):
                    valid = False
                    break

            if valid:
                ans += k

        return ans