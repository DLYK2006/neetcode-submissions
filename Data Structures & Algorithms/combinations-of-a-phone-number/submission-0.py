class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.keypad = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        self.results=[]
        current=""
        self.helper(current,0,0,digits)
        if digits=="":
            return []
        else:
            return self.results

    def helper(self,current,i,j,digits):
        print(current)

        if len(current)==len(digits):
            self.results.append(current)
            return 

        for j in range (len(self.keypad[int(digits[i])])):
            current+=self.keypad[int(digits[i])][j]
            self.helper(current,i+1,j+1,digits)
            current=current[:-1]
            
