
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(a, b) for a, b in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []
        stack.append(cars[0])
        for p, v in cars[1:]:
            if (target-p)/v <= (target-stack[-1][0])/stack[-1][1]:
                continue
            stack.append((p,v))
        return len(stack)
                
        

