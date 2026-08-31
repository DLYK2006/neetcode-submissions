class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        right=-1
        while right>-len(digits)-1:
            if digits[right]<9:
                digits[right]=digits[right]+1
                return digits
            else:
                digits[right]=0
            right-=1
        
        digits.insert(0,1)
        return digits

            
