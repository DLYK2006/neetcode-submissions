class Solution:
    def rob(self, nums: list[int]) -> int:
        # Edge case: if there is only 1 house, return its value immediately
        if len(nums) == 1: 
            return nums[0]
        
        # Define the inner function FIRST before calling it
        def dfs(i, end_index, cache):
            if i > end_index:
                return 0
            if cache[i] != -1:
                return cache[i]
            
            # Recurrence relation: rob current house or skip it
            cache[i] = max(nums[i] + dfs(i + 2, end_index, cache), dfs(i + 1, end_index, cache))
            return cache[i]
        
        # Scenario 1: Rob from the first house up to the second-to-last house
        cache1 = [-1] * len(nums)
        ans1 = dfs(0, len(nums) - 2, cache1)
        
        # Scenario 2: Rob from the second house up to the very last house
        cache2 = [-1] * len(nums)
        ans2 = dfs(1, len(nums) - 1, cache2)
        
        # The result is the maximum profit of both scenarios
        return max(ans1, ans2)
