class Solution:
    def countBits(self, n: int) -> List[int]:
        cache={}
        result=[]

        def get(i):
            if i==0:
                return 0
            
            if i in cache:
                return cache[i]

            cache[i]=get(i>>1)+(i&1)
            return cache[i]
        
        for i in range(n+1):
            result.append(get(i))
        
        return result