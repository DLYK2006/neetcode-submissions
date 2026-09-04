class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def adding(num1,num2):
            temp=""
            if len(num2)>len(num1):
                temp=num1
                num1=num2
                num2=temp
            ptr1=len(num1)-1
            ptr2=len(num2)-1
            carry=0
            result=[]
            
            while ptr1>=0 or ptr2>=0 or carry:
                if ptr1>=0:
                    d1=ord(num1[ptr1])-ord("0")
                else:
                    d1=0
                if ptr2>=0:
                    d2=ord(num2[ptr2])-ord("0")
                else:
                    d2=0
                total=d1+d2+carry
                carry=total//10
                result.append(str(total%10))
                ptr1-=1
                ptr2-=1
            
            return "".join(reversed(result))

        def mhelp(num1,digit,zeroes):
            mresult=[]
            ptr1=len(num1)-1
            carry=0
            if digit=="0":
                return "0"
            else:
                digit=ord(digit)-ord("0")
            
            while ptr1>=0 or carry:
                if ptr1>=0:
                    temp=ord(num1[ptr1])-ord("0")
                else:
                    temp=0
                total=(temp*digit)+carry
                carry=total//10
                mresult.append(str(total%10))
                ptr1-=1
            temp2="".join(reversed(mresult))
            for i in range(zeroes):
                temp2+="0"
            return temp2
        
        fr="0"
        if num1=="0" or num2=="0":
            return "0"
        else:
            for i in range(-1,-len(num2)-1,-1):
                padding=abs(i)-1
                digit=num2[i]
                partial=mhelp(num1,digit,padding)
                fr=adding(fr,partial)
            return fr


                
                

                

        

