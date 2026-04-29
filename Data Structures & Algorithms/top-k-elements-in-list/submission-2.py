class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary={}
        for num in nums:
            if num not in dictionary:
                dictionary[num]=1
            else:
                dictionary[num]+=1
        ranked=sorted(dictionary.items(),key=lambda x: x[1],reverse=True)
        output=[]
        for r in range(k):
            output.append(ranked[r][0])
        
        return output
        