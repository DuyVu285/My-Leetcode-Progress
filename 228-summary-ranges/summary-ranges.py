class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ans = []
        if not nums:
            return ans
        start = nums[0]
        end = nums[0]
        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                end = nums[i]
            else:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start)+"->"+str(end))
                start = nums[i]
                end = nums[i]
        if start == end:
            ans.append(str(start))
        else:
            ans.append(str(start)+"->"+str(end))
        return ans

            