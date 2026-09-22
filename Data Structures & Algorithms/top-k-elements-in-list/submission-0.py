class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico = {}
        for elem in nums:
            if elem in dico.keys():
                dico[elem] += 1
            else:
                dico[elem] = 1
        output = sorted(dico.items(), key=lambda x: x[1], reverse=True)
        cles_k = [cle for cle, _ in output[:k]]
        return cles_k