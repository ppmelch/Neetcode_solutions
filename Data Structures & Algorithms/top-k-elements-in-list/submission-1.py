class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        # Step 1: count frequencies
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        # Step 2: create buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        # Step 3: fill buckets
        for num, freq in freqMap.items():
            bucket[freq].append(num)

        # Step 4: collect top k
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
