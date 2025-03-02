class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        new_nums = defaultdict(int)
        for num_id, num in nums1:
            new_nums[num_id] += num
        for num_id, num in nums2:
            new_nums[num_id] += num
        result = [[key, value] for key, value in new_nums.items()]
        result.sort()
        return result
