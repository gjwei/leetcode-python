import string

class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
    
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,\
         41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        d = dict(zip(string.ascii_lowercase, prime))
        p_hash = 0
        for x in p:
            p_hash += d[x]
        result = []
        for i in xrange(len(s) - len(p)):
            current_substring_hash = 0
            for j in xrange(i, i + len(p)):
                current_substring_hash += d[s[j]]
            if current_substring_hash == p_hash:
                result.append(i)
        return result



    

if __name__ == '__main__':
    result = [2, 3]
    count = 2
    for i in xrange(4, 1000):
        is_prime = True
        for j in xrange(2, i - 1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            count += 1
            result.append(i)
        if count == 26:
                break
    print result
    print len(string.ascii_lowercase)
    
