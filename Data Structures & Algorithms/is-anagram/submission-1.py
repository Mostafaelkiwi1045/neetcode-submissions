class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # hashlest = list(s)
        # for i in t:
        #     if i in hashlest:
        #         hashlest.remove(i)
        #     else:
        #         return False
        # return len(hashlest) == 0

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)    

solution = Solution()
print(solution.isAnagram("racecar","carrace"))
print(solution.isAnagram("jar","jam"))
