
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # pass
        hash_alpha = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        d = defaultdict(list)
        for s in strs:
            hash_value = self.calculate_hash_value(s, hash_alpha)
            if hash_value not in d:
                d[hash_value] = [s]
            else:
                d[hash_value].append(s)
        result = []
        for key, value in d.iteritems():
            result.append(value)
        return result
            
            
    def calculate_hash_value(self, s, hash_alpha):
        result = 1
        for _, c in enumerate(s):
            result *= hash_alpha[ord(c) - ord('a')]
        return result


# import math

# def is_prime(n):
#     for i in xrange(2, n) :
#         if n % i == 0:
#             return False
#     return True

# if __name__ == '__main__':

#     result = [2, 3]
#     count = 2
#     while count < 26:
#         for i in xrange(4, 200):
#             if is_prime(i):
#                 result.append(i)
#                 count += 1
#     print result[:26]
            

