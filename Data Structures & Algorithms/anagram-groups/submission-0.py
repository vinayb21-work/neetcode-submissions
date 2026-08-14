class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            sortedStr = "".join(sorted(string))
            groups[sortedStr].append(string)
        return list(groups.values())