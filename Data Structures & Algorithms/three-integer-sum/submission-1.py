class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results=[]
        target=0
        front=1
        rear=len(nums)-1
        for i in range(len(nums)):
            front=i+1
            rear=len(nums)-1
            target=-nums[i]
            if i >0:
                if(nums[i]==nums[i-1]):
                    continue
            while rear>front:
                if(nums[front]+nums[rear]>target):
                    rear-=1
                elif(nums[front]+nums[rear]<target):
                    front+=1
                elif(nums[front]+nums[rear]==target):
                    results.append([nums[i],nums[front],nums[rear]])
                    front += 1
                    rear -= 1

                    while front < rear and nums[front] == nums[front - 1]:
                        front += 1

                    while front < rear and nums[rear] == nums[rear + 1]:
                        rear -= 1 
        return results