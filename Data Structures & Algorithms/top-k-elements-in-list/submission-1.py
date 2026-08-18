class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import statistics
        from collections import Counter
        result = [x for x, count in Counter(nums).most_common(k)]
        return result