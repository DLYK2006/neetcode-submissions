import string 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        back=-1
        real=s.replace(" ","").lower()
        translator = str.maketrans('', '', string.punctuation)
        real=real.translate(translator)
        print(real)
        for i in range(len(real)):
            if(real[i]==real[back]):
                back-=1
                continue
            else:
                return False
        return True