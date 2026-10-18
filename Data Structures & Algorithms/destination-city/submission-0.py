from collections import defaultdict

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        places=defaultdict(str)
        more=set()
        for a,b in paths:
            places[a]=b
            more.add(a)
            more.add(b)
        
        for i in more:
            if i not in places:
                return i
    
        
        
        
        
        pass
