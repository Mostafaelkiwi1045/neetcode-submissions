class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from statistics import mode
        result = []
        for i in range(k):
            m = mode(nums)
            result.append(m)
            nums = [x for x in nums if x != m]

        return result