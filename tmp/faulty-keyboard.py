
class Solution:
    def finalString(self, s: str) -> str:
        prev = ""
        for c in s:
            if c == 'i':
                prev = "".join(reversed(prev))
            else:
                prev = prev + c
        return prev
                
        
            
                
        
