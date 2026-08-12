class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for value in strs:
            sortedS = "".join(sorted(value))
            res[sortedS].append(value)
        return list(res.values())
            
        