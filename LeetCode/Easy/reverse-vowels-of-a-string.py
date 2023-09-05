class Solution:
    def reverseVowels(self, s: str) -> str:
        l, m, a = [], [], []

        for i in range(len(s)):
            c = s[i]
            if c in 'aeiouAEIOU':
                l.append("")
                m.append(i)
                a.append(c)
            else: l.append(c)

        m = m[::-1]

        for i in range(len(m)): l[m[i]] = a[i]
        return ''.join(l)
