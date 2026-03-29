class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for word in strs:
            # Sort the word to create a key
            key = "".join(sorted(word))

            # Group words with the same sorted key
            anagramMap[key].append(word)

        return list(anagramMap.values())