class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # We create a hashmap where:
        # key   → sorted version of the word
        # value → list of words that share the same sorted form (anagrams)
        anagramMap = defaultdict(list)

        # We iterate through each word in the input list
        for word in strs:

            # We sort the characters of the word
            # This works because anagrams have the same characters,
            # just in different order, so sorting makes them identical
            # Example:
            # "eat" → "aet"
            # "tea" → "aet"
            key = "".join(sorted(word))

            # We append the original word to the list corresponding to that key
            # If the key does not exist, defaultdict automatically creates an empty list
            anagramMap[key].append(word)

        # We return only the grouped values (lists of anagrams)
        # We don't need the keys anymore
        return list(anagramMap.values())