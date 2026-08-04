

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        total = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
            i += 1
        return total

