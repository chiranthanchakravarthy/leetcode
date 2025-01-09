class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        prefLen = len(pref)
        for word in words:
            if len(word) >= prefLen:
                if word[:prefLen] == pref:
                    count += 1
        return count