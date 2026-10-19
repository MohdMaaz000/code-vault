class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Modify board in-place.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    digit = board[r][c]
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[(r // 3) * 3 + c // 3].add(digit)

        def backtrack(pos):
            if pos == len(empty):
                return True

            r, c = empty[pos]
            box = (r // 3) * 3 + c // 3

            for digit in "123456789":
                if (digit not in rows[r]
                    and digit not in cols[c]
                    and digit not in boxes[box]):

                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box].add(digit)

                    if backtrack(pos + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box].remove(digit)

            return False

        backtrack(0)