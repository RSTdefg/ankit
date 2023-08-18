
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(sofar, num_open, remain):
            if remain == 0 and num_open == 0:
                result.append(sofar)
                return
            if remain < 0:
                return
            if num_open > 0:
                generate(sofar+')', num_open-1, remain)
            generate(sofar+'(', num_open+1, remain-1)
            return
        generate("", 0, n)
        return result
            
            

