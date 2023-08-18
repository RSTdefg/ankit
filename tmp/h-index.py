
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        while h < len(citations):
            if h + 1 > citations[h]:
                break
            h += 1
        return h
