class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_count, close_count):
            # If we have used all brackets
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add an opening bracket
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add a closing bracket
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result