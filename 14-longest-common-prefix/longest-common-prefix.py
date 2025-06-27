class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        comm_prefix = ""
        max_index = len(strs[0])

        try:
            for index in range(max_index):
                dict_letters={}
                for str in strs:
                    letter = str[index]
                    dict_letters[letter]  = dict_letters.get(letter,0) + 1
                if len(dict_letters) > 1:
                    break
                comm_prefix += letter

            return comm_prefix
        except:
            return comm_prefix