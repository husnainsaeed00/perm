class Solution:
    def getPermutation(self, n, k):
        available_digits = list(range(1, n + 1))
        factorials = [1]
        for i in range(1, n + 1):
            factorials.append(factorials[-1] * i)

        k -= 1
        result = []

        for i in range(n, 0, -1):
            index = k // factorials[i - 1]
            result.append(str(available_digits[index]))
            available_digits.pop(index)
            k %= factorials[i - 1]

        return ''.join(result)

# Test cases
solution = Solution()
print(solution.getPermutation(3, 3))  # Output: "213"
print(solution.getPermutation(4, 9))  # Output: "2314"
print(solution.getPermutation(3, 1))  # Output: "123"
