class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sortie = []
        produit = 1
        cpt = 0
        for elem in nums:
            if elem != 0:
                produit*=elem
            else:
                cpt += 1
        for elem in nums:
            if cpt > 1:
                sortie.append(0)
            elif elem == 0 :
                sortie.append(produit)
            else:
                if cpt == 0:
                    sortie.append(produit//elem)
                else:
                    sortie.append(0)
        return sortie