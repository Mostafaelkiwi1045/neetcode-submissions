class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return (len(nums)) != len(set(nums))

solution = Solution()
print(solution.hasDuplicate([1,2,3,4]))
print(solution.hasDuplicate([1,2,3,3]))        
