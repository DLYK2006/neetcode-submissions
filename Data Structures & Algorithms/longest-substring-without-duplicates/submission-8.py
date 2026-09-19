class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        longest=0
        seen=set()

        while right>=left:
            if right==len(s):
                break
            
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
                
            longest=max(right-left,longest)
        return(longest)
            

            



        
        