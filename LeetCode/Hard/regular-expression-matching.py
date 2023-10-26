import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        f = "*".join(" ".join(p.split("*")).split())
        if p[-1] == '*': f += '*'
        c = re.compile(f).findall(s)
        l = []

        for i in c:
            if i != '': l.append(i)

        return True if len(l) == 1 and "".join(l) == s else False
