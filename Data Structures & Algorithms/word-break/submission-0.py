class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache={}

        def helper(i):
            if i==len(s):
                return True
            
            if i in cache:
                return cache[i]

            for w in wordDict:
                if s[i:i+len(w)]==w:
                    result=helper(i+len(w))
                    if result:
                        cache[i]=result
                        return result
            cache[i]=False
            return False
        return helper(0)
                


            
