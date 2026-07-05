class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        else:
            anagrams = []
            used_indices = set()  # Set to track used indices

            for i in range(len(strs)):
                if i not in used_indices:
                    current_anagram_group = [strs[i]]
                    used_indices.add(i)
                    for j in range(i + 1, len(strs)):
                        if j not in used_indices and sorted(strs[i]) == sorted(strs[j]):
                            current_anagram_group.append(strs[j])
                            used_indices.add(j)
                    anagrams.append(current_anagram_group)

            return anagrams

        