
import bisect
class TimeMap:

    def __init__(self):
        self.li = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.li[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        index = bisect.bisect(self.li[key], timestamp, key = lambda x:x[0])-1
        if index < 0:
            return ""
        return self.li[key][index][1]
        
        


