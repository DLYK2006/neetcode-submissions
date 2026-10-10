class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache={}

        def helper(i):
            if i==len(s):
                return True
            
            if i in cache:
                return cache[i]

            for m in wordDict:
                if s[i:i+len(m)]==m:
                    result=helper(i+len(m))
                    if result:
                        cache[i]=result
                        return result
            cache[i]=False
            return False

        return helper(0)