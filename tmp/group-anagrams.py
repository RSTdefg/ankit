
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)
        for str in strs:
            m[tuple(sorted(str))].append(str)
        return m.values()
        
