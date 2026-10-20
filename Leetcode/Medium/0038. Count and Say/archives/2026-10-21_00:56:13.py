class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            result = []
            i = 0

            while i < len(s):
                j = i

                while j < len(s) and s[j] == s[i]:
                    j += 1

                result.append(str(j - i) + s[i])
                i = j

            s = "".join(result)

        return s