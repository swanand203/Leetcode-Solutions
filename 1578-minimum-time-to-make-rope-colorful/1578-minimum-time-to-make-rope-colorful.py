class Solution:
  def minCost(self, colors: str, neededTime: List[int]) -> int:
    ans = 0
    maxNeededTime = neededTime[0]

    for i in range(1, len(colors)):
      if colors[i] == colors[i - 1]:
        ans += min(maxNeededTime, neededTime[i])
        maxNeededTime = max(maxNeededTime, neededTime[i])
      else:
        maxNeededTime = neededTime[i]

    return ans        