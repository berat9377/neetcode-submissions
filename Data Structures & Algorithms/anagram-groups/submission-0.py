class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        out = {}

        for string in strs:
            out.setdefault(str(sorted(string)), []).append(string)

        return list(out.values())