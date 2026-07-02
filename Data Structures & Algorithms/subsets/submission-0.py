class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results=[]
        current=[]
        self.array=nums
        if len(nums)==0:
            return self.results
        self.helper(0,current)
        return self.results

    def helper(self,i,current):
        if i==len(self.array):
            self.results.append(current.copy())
            return current
        current.append(self.array[i])
        self.helper(i+1,current)
        current.pop()
        self.helper(i+1, current)
        