class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        for i in range(max(len(word1), len(word2))):
            try: s += word1[i]
            except: pass

            try: s += word2[i]
            except: pass
        
        return s
