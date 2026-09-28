class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
            
        nums.sort()
        
        # Greedy check function
        def can_form_p_pairs(max_diff: int) -> bool:
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # Skip both elements used in the pair
                else:
                    i += 1  # Skip only the left element
                
                if count >= p:
                    return True
            return False

        # Binary search range for the answer
        left, right = 0, nums[-1] - nums[0]
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if can_form_p_pairs(mid):
                ans = mid
                right = mid - 1  # Try to find a smaller maximum difference
            else:
                left = mid + 1   # Difference too tight, increase threshold

        return ans