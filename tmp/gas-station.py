
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        roll, result = 0, 0
        sumi = 0
        for i, (a, b) in enumerate(zip(gas, cost)):
            if roll < 0:
                roll = 0
                result = i
            roll += a - b
            sumi += a - b
        return result if sumi >= 0 else -1

