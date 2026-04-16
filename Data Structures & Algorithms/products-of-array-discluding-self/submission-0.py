class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        for i in range(len(nums)):

            total = 1

            for j in range(len(nums)):

                if i != j:
                    total *= nums[j]

            result.append(total)

        return result