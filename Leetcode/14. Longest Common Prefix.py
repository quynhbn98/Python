# Write a function to find the longest common prefix string amongst an array of strings.
# https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(self, strs: List[str]) -> str:
    commonprefix_list = []
    commonprefix_element = ''
    commonprefix = ''
    length = set([])
    if strs == []:
        return ''
    else:
        for i in range(len(strs)):
            length.add(len(strs[i]))
        for i in range(min(length)):
            for j in range(len(strs)):
                commonprefix_element += strs[j][i]
            commonprefix_list.append(commonprefix_element)
            commonprefix_element = ''
        for i in commonprefix_list:
            if i.count(i[0]) == len(i):
                commonprefix += i[0]
            else:
                break
        return commonprefix
