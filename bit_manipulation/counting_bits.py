def countBits(self, n: int) -> List[int]:

  dp = [0] * (n + 1)
  offset = 1

  for i in range (1, n + 1):
      if offset * 2 == i:
          offset = i
      dp[i] = 1 + dp[i - offset]
  return dp
'''
1  0 0 0 1
2  0 0 1 0
3  0 0 1 1
4  0 1 0 0
5  0 1 0 1
6  0 1 1 0
7
8  1 0 0 0
9

16 1
'''
