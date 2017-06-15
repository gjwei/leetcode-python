"""Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split(r'/')
        print path_list
        stack = []
        for i, dir in enumerate(path_list):
            if dir == '' or dir == '.':
                continue
            elif dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return '/' + '/'.join(stack)

s = Solution()
print s.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///")
        