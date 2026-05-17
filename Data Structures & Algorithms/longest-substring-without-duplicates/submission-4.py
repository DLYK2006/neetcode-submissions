class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        right=0
        longest=0

        while right<len(s):
            print(seen)
            if s[right] in seen:
                seen.remove(s[left])
                left+=1
                continue
            if s[right] not in seen:
                seen.add(s[right])
                longest=max(longest,right-left+1)
            right+=1
            
        return longest
            
