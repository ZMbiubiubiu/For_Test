"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词

输入: s = "anagram", t = "nagaram"
输出: true

输入: s = "rat", t = "car"
输出: false
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # method 1.排序法
        # return sorted(s) == sorted(t)
        # method 2.map映射法
        """
        map1 = self.map(s)
        map2 = self.map(t)
        return map1 == map2
    def map(self, s):
        hashmap = {}
        for i in s:
            try:
                hashmap[i] += 1
            except:
                hashmap[i] = 1
        return hashmap
        """
        # method 3.map映射法2
        """
        map1, map2 = {}, {}
        for i in s:
            map1[i] = map1.get(i, 0) + 1
        for j in t:
            map2[j] = map2.get(j, 0) + 1
        return map1 == map2
        """
        # method 4.桶排序法
        buck1, buck2 = [0] * 26, [0] * 26
        ord_a = ord('a')
        for i in s:
            buck1[ord(i) - ord_a] += 1
        for j in t:
            buck2[ord(j) - ord_a] += 1
        return buck1 == buck2


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))