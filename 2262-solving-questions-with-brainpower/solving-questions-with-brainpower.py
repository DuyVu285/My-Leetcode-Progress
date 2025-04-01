class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [-1] * n 

        def calculatePointsRecursion(current_index: int) -> int:
            if current_index >= n:
                return 0

            if dp[current_index] != -1:
                return dp[current_index]

            points, brainpower = questions[current_index]

            answer = points + calculatePointsRecursion(current_index + brainpower + 1)

            skip = calculatePointsRecursion(current_index + 1)

            dp[current_index] = max(answer, skip)

            return dp[current_index]

        # Start the recursion from index 0
        return calculatePointsRecursion(0)
