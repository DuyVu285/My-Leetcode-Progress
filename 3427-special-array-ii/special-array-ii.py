class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        if n < 2:
            return [True] * len(queries)  # Single element or empty arrays are always "special"
        
        # Step 1: Precompute adjacency parity differences
        diff = [1 if nums[i] % 2 != nums[i + 1] % 2 else 0 for i in range(n - 1)]
        
        # Step 2: Compute prefix sums
        prefix = [0] * (n - 1)
        prefix[0] = diff[0]
        for i in range(1, n - 1):
            prefix[i] = prefix[i - 1] + diff[i]
        
        # Step 3: Process queries
        ans = []
        for fromi, toi in queries:
            if toi == fromi:
                # A single-element subarray is always "special"
                ans.append(True)
                continue
            
            # Calculate the sum of `diff` over the range [fromi, toi - 1]
            range_sum = prefix[toi - 1] - (prefix[fromi - 1] if fromi > 0 else 0)
            # Check if all differences are valid
            ans.append(range_sum == (toi - fromi))
        
        return ans