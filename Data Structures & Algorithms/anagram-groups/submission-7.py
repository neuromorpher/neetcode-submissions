class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) #map charCount to [list of anagrams]

        for s in strs:

            count = [0]*26 #[0,0,0,0...0,0]_26

            for c in s:

                count[ord(c) - ord("a")] += 1 #[1,1,0...1,0,0] --> # [3,7,0...,2,0,1]

            res[tuple(count)].append(s)

        return list(res.values())





        

