
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if not stack or stack[-1] < 0 or ast > 0:
                stack.append(ast)
                continue
            while stack and stack[-1] > 0:
                if abs(stack[-1]) == abs(ast):
                    stack.pop()
                    break
                elif abs(stack[-1] < abs(ast)):
                    stack.pop()
                    if not stack or stack[-1] < 0:
                        stack.append(ast)
                        break
                elif abs(stack[-1] > abs(ast)):
                    break
                
                    
        return stack
                
                





        
