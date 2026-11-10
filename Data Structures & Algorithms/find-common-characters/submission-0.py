class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        frequency=defaultdict(int)

        for i in words[0]:
            frequency[i]+=1
        
        for w in words:
            bruh=Counter(w)
            for key,value in frequency.items():
                frequency[key]=min(bruh[key],frequency[key])
        
        ans=[]
        for key,value in frequency.items():
            for i in range(frequency[key]):
                ans.append(key)
        
        return ans