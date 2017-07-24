# [bit manipulations](https://discuss.leetcode.com/topic/50315/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently)


## 1. basic
1. set Union A | B
2. set intersection A & B
3. set subtraction A & ~B A去除B中的位
4. Set negation ALL_BITS ^ A or ~A
5. set bit A |= 1 << bit
6. clear bit A &= ~(1 << bit)
7. test bit (A &  (1 << bit)) != 0
8. extract last bit A & -A or A & ~(A - 1) or x ^ (x & (x - 1))
9. remove last bit A & (A - 1)
10. get all 1-bits ~0

## 2. Examples

```
int count_one(int n) {
    while(n) {
        n = n & (n-1);
        //这句话的意思：出去最后一位1
        count++;
    }
    return count;
}
```

2. is power of four
```
bool is_power_of_four(int n) {
    //4的次方，二进制只有一位，而且位数均在奇数的位置
    return !(n & (n - 1)) && (n & 0x55555555);
}
```

##3. ^ trick
MISSING NUM
```python
def missing_number(nums) :
    result = 0
    for i in xrange(0, len(nums)):
        result ^= i
        result ^= nums[i]
    return result ^ len(nums)

    
```

##4. | trick
find the largest power of 2
```python
def largest_power(n):
    n = n | (n >> 1)
    n = n | (n >> 2)
    n = n | (n >> 4)
    n = n | (n >> 8)
    n = n | (n >> 16)
    return (n + 1) >> 1

    
```

##5. reverse bits
reverse bits of 32bits unsigned integer

```python
def reverse_bits(n) :
    mask = 1 << 31
    result = 0
    for i in xrange(32):
        if n & i == 1:
            result |= mask
        mask >>= 1
        n >>= 1
    return result
```

##6. & trick
selection certain bits
Reverseing bits in integer

```python
x = ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1)
x = ((x & 0xcccccccc) >> 2) | ((x & 0x33333333) << 2)
x = ((x & 0xf0f0f0f0) >> 4) | ((x & 0x0f0f0f0f) << 4)
x = ((x & 0xff00ff00) >> 8) | ((x & 0x00ff00ff) << 8)
x = ((x & 0xffff0000) >> 16) | ((x & 0x0000ffff) << 16)
```

##7. BITWISE AND OF NUMBERS RANGE

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive. For example, given the range [5, 7], you should return 4.

```java
int rangeBitwiseAnd(int m, int n) {
    int a = 0;
    while(m != n) {
        m >>= 1;
        n >>= 1;
        a++;
    }
    return m<<a; 
}
```

##8. NUMBER OF 1 BITS

```python
def count_bits(n):
    result = 0
    while n:
        n &= (n - 1)
        result += 1
    return result
```

## 9. Application

### 1. REPEATED DNA SEQUENCES

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA. Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
For example,
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
Return: ["AAAAACCCCC", "CCCCCAAAAA"].

```python
def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {'A': 1, 'C':2, 'G':3, 'T': 4}
        help_dict = {}
        result = []
        for i in xrange(len(s)):
            dna = self.encode_dna(s[i:i+10], d)
            if dna in help_dict and help_dict[dna] == 1:
                result.append(s[i:i+10])
            help_dict[dna] = help_dict.get(dna, 0) + 1
        return result
         
    def encode_dna(self, s, d):
        result = 0
        for i, c in enumerate(s):
            result += (d[c]) << 2 * i
        return result
```

### 2. MAJORITY ELEMENT

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times. (bit-counting as a usual way, but here we actually also can adopt sorting and Moore Voting Algorithm)

###### Solution

```python
#思想很简单，统计数组中第i个位的1和0的个数，比较二者大小，大的为大于一半的数的位
def majority_element(nums):
    result = 0
    for i in xrange(32):
        ones, zeros = 0, 0
        for n in nums:
            if n >> i & 1:
                ones += 1
            else:
                zeors += 1
         if ones > zeros:
            result += 1 << i
     return result

```

### 3 SINGLE NUMBER III

Given an array of integers, every element appears three times except for one. Find that single one. (Still this type can be solved by bit-counting easily.) But we are going to solve it by `digital logic design`

###### Solution

```python
#和上一个题目相同的思路
def single_numberIII(nums):
    result = 0
    for i in xrange(32):
        ones = 0
        for n in nums:
            ones += nums >> i & 1
        if ones % 3 == 1:
            result += 1 << i
     return result
```

还有一种答案，但是我没有看懂，他说的是：digital logic design的方法进行解决的

```python
def singleNumber(nums):
    t, a, b = 0, 0, 0
    for n in nums:
        t = (a & ~b & ~n) | (~a & b & n)
        b = (~a & b & ~n) | (~a & ~b & n)
        a = t
     return a | b
```

### 4 MAXIMUM PRODUCT OF WORD LENGTHS

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

> Example 1:
> Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
> Return 16
> The two words can be "abcw", "xtfn".

> Example 2:
> Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
> Return 4
> The two words can be "ab", "cd".

> Example 3:
> Given ["a", "aa", "aaa", "aaaa"]
> Return 0
> No such pair of words.

###### Solution

```python
def max_product(words):
    mask = [0 for _ in xrange(len(words))]
    result = 0
    for i in xrange(len(words)):
        for c in words[i]:
            mask[i] |= 1 << (ord(c) - ord('a') + 1)
        for j in xrange(i):
            if mask[i] & mask[j] == 0:
                result = max(result, len(words[i]) * len(words[j]))
    return result
```

## Attention

- result after shifting left(or right) too much is undefined
- right shifting operations on negative values are undefined
- right operand in shifting should be non-negative, otherwise the result is undefined
- The & and | operators have lower precedence than comparison operators

## SETS

**All the subsets **

所有的子集
A big advantage of bit manipulation is that it is trivial to iterate over all the subsets of an N-element set: every N-bit value represents some subset. Even better, `if A is a subset of B then the number representing A is less than that representing B`, which is convenient for some dynamic programming solutions.

位操作的一大优点是迭代N元素集合的所有子集都是微不足道的：每个N位值代表一些子集。 更好的是，如果A是B的子集，则表示A的数字小于表示B的数字，这对于一些动态编程解决方案是方便的。

It is also possible to iterate over all the subsets of a particular subset (represented by a bit pattern), provided that you don’t mind visiting them in reverse order (if this is problematic, put them in a list as they’re generated, then walk the list backwards). The trick is similar to that for finding the lowest bit in a number. If we subtract 1 from a subset, then the lowest set element is cleared, and every lower element is set. However, we only want to set those lower elements that are in the superset. So the iteration step is just `i = (i - 1) & superset`.

如果您不介意以相反的顺序访问它们（如果这是有问题的，则将它们放在列表中，因为它们被生成），也可以遍历特定子集的所有子集（由位模式表示） ，然后向后走列表）。 这个技巧类似于在数字中找到最低位的技巧。 如果我们从子集中减去1，那么最低的集合元素被清除，并且每个下一个元素被设置。 但是，我们只想设置超集中的较低元素。 所以迭代步骤只是`i =（i - 1）＆ superset`

```python
def subset(s):
    s = sorted(s)
    total = 1 << len(s)
    result = []
    for i in xrange(total):
       	l = []
        for j in xrange(len(s)):
            if (i >> j) & 1 == 1:
                l.append(s[j])
        result.append(l)
     return result
```

Actually there are two more methods to handle this using `recursion` and `iteration` respectively.



## BITSET

A [bitset](http://www.cplusplus.com/reference/bitset/bitset/?kw=bitset) stores bits (elements with only two possible values: 0 or 1, true or false, ...).
The class emulates an array of bool elements, but optimized for space allocation: generally, each element occupies only one bit (which, on most systems, is eight times less than the smallest elemental type: char).