class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        else:
            anagrams = []
            used = [False] * len(strs)  # Track which strings have been grouped

            for i in range(len(strs)):
                if not used[i]:
                    current_anagram_group = [strs[i]]
                    used[i] = True
                    for j in range(i + 1, len(strs)):
                        if sorted(strs[i]) == sorted(strs[j]):
                            current_anagram_group.append(strs[j])
                            used[j] = True
                    anagrams.append(current_anagram_group)

            return anagrams

        