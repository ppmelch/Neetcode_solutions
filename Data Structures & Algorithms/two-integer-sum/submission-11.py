class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This problem requires an efficient solution better than O(n²),
        # so we use a hashmap to achieve O(n) time complexity.

        prevMap = {}  # Stores value → index (space complexity O(n))

        # We iterate through the array once → O(n)
        for i, num in enumerate(nums):

            # For each element, we compute the complement needed
            # to reach the target
            diff = target - num

            # We check if we have already seen this complement
            # This lookup is O(1) on average
            if diff in prevMap:
                # If found, we return the indices:
                # previous index (stored in hashmap) + current index
                return [prevMap[diff], i]

            # Otherwise, we store the current number with its index
            prevMap[num] = i

        # Time Complexity: O(n) → single pass through the array
        # Space Complexity: O(n) → storing elements in hashmap
        