class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets=[]
        ans=[]
        def dfs(ans,i):
            if i==len(nums) :
                subsets.append(ans.copy())
                return
            ans.append(nums[i])
            dfs(ans,i+1)
            ans.pop()
            dfs(ans,i+1)

        dfs(ans,0)
        return subsets