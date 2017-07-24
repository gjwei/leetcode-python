class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        bin_num = self.toBin(num)
        result = []
        for i in xrange(0, 32, 4):
            t = self.get_hex(bin_num[i:i+4])
            # print bin_num[i:i +4], t
            if t == '0' and len(result) == 0:
                continue
            result.append(t)
        return ''.join(result)
    
    def get_hex(self, s):
        count = 0
        for i in xrange(4):
            count += int(s[i]) * (2 ** (3 - i))
        return str(count) if 0 <= count <= 9 else chr(count - 10 + ord('a'))        
        
    def toBin(self, num):
        is_negative = num < 0
        if is_negative: 
            num = -num
        result = [0 for _ in xrange(32)]
        for i in xrange(31):
            result[i] = num >> i & 1
            result[i] = 1 - result[i] if is_negative else result[i]
        # print result
        if is_negative:
            carry = 1
            for i in xrange(31):
                t =result[i]
                result[i] = (t + carry) % 2
                carry = (t + carry) // 2
                
        result[31] = 1 if is_negative else 0
        return ''.join([str(i) for i in result[::-1]])
            
            
        
s = Solution()
print s.toHex(-1)