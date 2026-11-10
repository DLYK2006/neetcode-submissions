import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products=sorted(products)
        answer=[]
        prefix=""
        for i in searchWord:
            prefix+=i
            grah=bisect.bisect_left(products,prefix)
            post=[]
            print(grah)
            for j in range(grah,min(grah+3,len(products))):
                if products[j].startswith(prefix):
                    post.append(products[j])
                else:
                    break
            answer.append(post)
        return answer

        pass
