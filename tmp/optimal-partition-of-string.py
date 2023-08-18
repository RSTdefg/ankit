
class Solution:
    def partitionString(self, s: str) -> int:
        se = set()
        result = []
        cur = ""
        for c in s:
            if c not in se:
                se.add(c)
                cur+=c
            else:
                result.append(cur)
                se = {c}
                cur = c
        return len(result)+1


