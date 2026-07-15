class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for s in strs:
            out += f'{len(s)} {s}'
        return out

    def decode(self, s: str) -> List[str]:
        i = 0
        out = []
        while i<len(s):
            length = ''
            while s[i] != ' ':
                length += s[i]
                i+=1
            num = int(length)
            out.append(s[i+1:i+1+num])
            i += 1+num
        return out
