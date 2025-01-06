class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        count = 0
        steps = 0

        for i in range(n):
            answer[i] += steps
            count += int(boxes[i])
            steps += count
        
        count = 0
        steps = 0
        for i in range(n-1,-1,-1):
            answer[i] += steps
            count += int(boxes[i])
            steps += count
        
        return answer