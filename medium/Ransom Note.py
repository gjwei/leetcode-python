class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_index, m_index = 0, 0
        while r_index < len(ransomNote) and m_index < len(magazine):
            if ransomNote[r_index] == magazine[m_index]:
                r_index += 1
            m_index += 1
        if r_index == len(ransomNote):
            return True
        return False
            
            
s = Solution()
a = "bjaajgea"
b = "affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec"
print s.canConstruct(a, b)
