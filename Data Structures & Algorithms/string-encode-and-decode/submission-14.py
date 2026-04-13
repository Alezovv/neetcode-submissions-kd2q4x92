class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for x in strs:
            n = len(x)
            result += str(n) + '#'
            result += x
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        len_s = len(s)
        i = 0
        result = []
        print(s)
        while i < len_s:
            n = ""
            substring = ""
            #isLen = 1
            while s[i].isdigit() and s[i] != '#':
                #isLen = 0
                n += s[i]
                i += 1
            print("Длина подстроки: ", n)
            i += 1
            j = 0
            while j != int(n):
                substring += s[i]
                i += 1
                j += 1
            print(substring)
            result.append(substring)

        return result
