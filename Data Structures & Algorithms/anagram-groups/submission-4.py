class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hasMap = defaultdict(list)

        for i in strs: 
            key = "".join(sorted(i))
            hasMap[key].append(i)
        return list(hasMap.values())




        