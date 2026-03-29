class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lista=defaultdict(list)
        for i in strs:
            sort = ''.join(sorted(i))
            lista[sort].append(i)
        return list(lista.values())

        