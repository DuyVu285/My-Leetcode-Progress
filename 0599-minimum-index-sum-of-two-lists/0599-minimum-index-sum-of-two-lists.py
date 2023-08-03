class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = {}
        
        for i, word in enumerate(list1):
            if word in list2:
                index_sum = i + list2.index(word)
                if word not in result:
                    result[word] = index_sum
                else:
                    result[word] = min(result[word], index_sum)
        
        min_index_sum = min(result.values())
        
        common_strings = [word for word, index_sum in result.items() if index_sum == min_index_sum]
        
        return common_strings