class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in hashTable:
                hashTable[key].append(s)
            else:
                hashTable[key] = [s]
        return hashTable.values()