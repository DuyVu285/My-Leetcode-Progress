class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        # Step 2 to 5: Iterate through the dictionary and find the longest harmonious subsequence
        max_length = 0
        for num in freq_dict:
            if num + 1 in freq_dict:
                length = freq_dict[num] + freq_dict[num + 1]
                max_length = max(max_length, length)

        return max_length