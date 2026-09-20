class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        bruh = "".join(char for char in s if char.isalnum()).lower()
        left=0
        right=len(bruh)-1
        print(bruh)

        while right>=left:
            if bruh[right]==bruh[left]:
                right-=1
                left+=1
            else:
                return False
        
        return True