
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(cur):
            l, r = 0, len(cur)-1
            while l <= r:
                if cur[l] != cur[r]:
                    return False
                l += 1
                r -= 1
            return True
        result = []
        def recur(index, cur):
            if index > len(s):
                return
            if index == len(s):
                result.append(cur)
                return
            for i in range(index+1, len(s)+1):
                if check(s[index:i]):
                    recur(i, cur+[s[index:i]])
            return
        recur(0, [])
        return result


