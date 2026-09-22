class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = {}
        output = []
        for elem in strs:
            cle = "".join(sorted(elem))
            if cle in dico:
                dico[cle].append(elem)
            else:
                dico[cle] = [elem]
        return list(dico.values())