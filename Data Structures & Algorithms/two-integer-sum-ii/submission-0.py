class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        gauche, droite = 0, len(numbers) - 1
        somme = numbers[gauche] + numbers[droite]
        while somme != target :
            if somme > target :
                droite -= 1
            elif somme < target :
                gauche += 1
            somme = numbers[gauche] + numbers[droite]
        return [gauche+1, droite+1]