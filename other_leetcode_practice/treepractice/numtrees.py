class Solution:
    def numTrees(self, n: int) -> int:
        dp_table = [0] * (n+1)
        dp_table[1] = 1
        dp_table[0] = 1
        if n == 1:
            return 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp_table[i] += (dp_table[j] * dp_table[i-j-1])
        return dp_table[n]