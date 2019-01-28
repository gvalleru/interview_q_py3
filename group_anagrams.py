from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        # create default dict. of list
        my_dict = defaultdict(list)
        for str_ in strs:
            # sort the sting and make the sorted string as key
            # then added strings to that key
            my_dict[''.join(sorted(str_))].append(str_)
        return my_dict.values()
