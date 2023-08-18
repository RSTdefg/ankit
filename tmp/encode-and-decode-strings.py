
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        payload = [",".join([str(ord(c)) for c in s]) for s in strs]
        return ".".join(payload)
         

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        payload = s.split('.')
        print(payload)
        res = ["".join([chr(int(c)) if c else "" for c in s.split(',')]) for s in payload]
        return res
        
        


