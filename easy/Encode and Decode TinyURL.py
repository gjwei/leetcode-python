import string
import random

class Codec:

    def __init__(self):
        self.encode_to_decode = {}
        self.decode_to_encode = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        shortUrl = self.get_random_short_url(longUrl)
        self.encode_to_decode[shortUrl] = longUrl
        # decode_to_encode
        return shortUrl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.encode_to_decode[shortUrl]


    def get_random_short_url(self, longUrl):
        short_url_begin = 'http://tinyurl.com/'
        return short_url_begin + self.get_random_short_url(len(random) // 4)

    
    def get_random_string(self, n):
        if n == 0:
            n = 1
        d = string.ascii_letters + string.digits
        result = []
        while n:
            result.append(random.choice(d))
        return ''.join(result)

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))