
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {2:"abc",3:"def",4:"ghi",5:"jkl", 6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        result = []
        def go(i, sofar):
            if i == len(digits):
                if sofar:
                    result.append(sofar)
                return
            
            for c in m[int(digits[i])]:
                go(i+1, sofar+c)
        go(0, "")
        return result


            
