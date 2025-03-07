class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        limit = right + 1  # To include 'right' in the sieve
        is_prime = [True] * (limit)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

        for i in range(2, int(limit ** 0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, limit, i):
                    is_prime[multiple] = False
        
        # Step 2: Collect primes in the given range
        primes = [num for num in range(left, right + 1) if is_prime[num]]

        # Step 3: Find the closest pair
        if len(primes) < 2:
            return [-1, -1]  # No valid pair found
        
        min_diff = float('inf')
        result = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i], primes[i + 1]]

        return result