class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency=defaultdict(int)
        letters=defaultdict(int)
        count=2
        cc=1
        result=0

        for i in word:
            frequency[i]+=1

        wow = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        for letter,freq in wow:
            if letter not in letters:
                letters[letter]=cc
                count+=1
            if count==10:
                count=2
                cc+=1
        print(letters)
        for i in word:
            result+=letters[i]
        
        return(result)
        pass
