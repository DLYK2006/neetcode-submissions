class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency=defaultdict(int)
        result=[]

        for i in nums:
            frequency[i]+=1

        sorted_desc = list(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        
        
        for i in range(k):
            result.append(sorted_desc[i][0])
        
        
        return result
        