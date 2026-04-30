class Solution:

    def encode(self, strs: List[str]) -> str:
        secret=''

        for i in range(len(strs)):
            length=len(strs[i])
            secret+=str(length)
            secret+='—'
            secret+=strs[i]
        
        return secret

    def decode(self, s: str) -> List[str]:
        print(s)
        count=s.count('—')
        size=''
        output=[]
        i=0
        for m in range(count):    
            for a in range(i,len(s)):
                if s[a]=='—':
                    break
                size+=str(s[a])
            size=int(size)
            start=int(a)+1
            end=start+size
            actual=s[start:end]
            output.append(actual)
            print(actual)
            i=end
            size=str(size)
            size=''
        return output


    