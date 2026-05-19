class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False
        
        left=0
        right=len(s1)
        counts={}
        counts2={}

        for i in range(len(s1)):
            counts[s1[i]]=1 + counts.get(s1[i],0)
        print(counts)

        for i in range(right):
            counts2[s2[i]]=1 + counts2.get(s2[i],0)


        for i in range(len(s1),len(s2)):
            if(counts==counts2):
                return True
            print(counts2)
            counts2[s2[right]]=1 + counts2.get(s2[right],0)
            counts2[s2[left]]-=1
            if(counts2[s2[left]]==0):
                del counts2[s2[left]]
            right+=1
            left+=1
            print(counts2)

        if(counts==counts2):
            return True
        else:
            return False