class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_real, a_image = self.get_real_and_image(a)
        b_real, b_image = self.get_real_and_image(b)
        result_real = a_real * b_real - a_image * b_image
        result_image = a_real * b_image + a_image * b_real
        return str(result_real) + '+' + str(result_image) + 'i'
    def get_real_and_image(self, a):
        positive_sign = a.find('+')
        return int(a[:positive_sign]), int(a[positive_sign+1:-1])
