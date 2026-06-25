class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {"".join(sorted(x)):[] for x in strs}    
        for word in strs:
            check = "".join(sorted(word))
            if check in sorted_strs:
                sorted_strs[check].append(word)
        return list(sorted_strs.values())