class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This is a problem that it needs to be satisfied by time O(1) and complexity O(1)
        prevMap = {}
        for i , j in enumerate(nums):
            diff = target - j
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[j] = i

