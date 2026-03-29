class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Its a problem that we need to find a solution with O(n) time and O(n) space.
        # For this , we iterate in i and j to find the pair of indices that satisfy the condition.
        # 1. A loop that for each indice in the range of the nums.
        for i in range(len(nums)):
            # 2. We start from i + 1 to avoid duplicate pairs and ensure we don’t compare an element with itself.
            for j in range(i+1 ,len(nums)):
                # if the two conditions are fulfilled , then we return the pair of indices.
                if nums[i] + nums[j] == target and i!=j :
                    return [i,j]
        # We know that , this code is O(n) because it process each element once
