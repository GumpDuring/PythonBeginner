class Solution(object):
    def __init__(self):
        pass
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = [0]*26
        i = 0
        while i < len(s):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1
            i += 1
        j = 0
        while j < 26:
            if count[j] != 0:
                return False
            j += 1

        return True


# class Solution(object):
#     def __init__(self):
#         pass
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         count1 = [0]*26
#         i1 = 0
#         while i1 < len(s):
#             count1[ord(s[i1])-ord('a')] += 1
#             i1 += 1
#         formation1 = []
#         j1 = 0
#         while j1 < 26:
#             if count1[j1]:
#                 formation1.append(chr(j1+ord('a'))*count1[j1])
#             j1 += 1

#         count2 = [0]*26
#         i2 = 0
#         while i2 < len(t):
#             count2[ord(t[i2])-ord('a')] += 1
#             i2 += 1
#         formation2 = []
#         j2 = 0
#         while j2 < 26:
#             if count2[j2]:
#                 formation2.append(chr(j2+ord('a'))*count2[j2])
#             j2 += 1

#         if formation1 == formation2:
#             return True
#         else:
#             return False

# a = Solution()
# a.isAnagram(s = "rat", t = "car")
#这是最初的思考。我用了两次计数器，意味着两次遍历，浪费时间资源，而且formation是多余的。
#既然使用了计数器，就在计数器的基础上改变，没必要引入新东西。做差就是最快的办法。
#而且这里的长度不等和j遍历时遇到非零就提前退出是非常值得学习的做法，将复杂度尽可能缩小。
