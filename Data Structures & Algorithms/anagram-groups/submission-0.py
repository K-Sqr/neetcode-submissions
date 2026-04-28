class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result =[]
        maps = {}
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in maps:
                maps[sorted_string].append(s)
            else:
                maps[sorted_string] = [s]
        return list(maps.values())



        
        