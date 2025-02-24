class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            # If asteroid is moving right, push it onto the stack
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # Handle collisions
                while stack and stack[-1] > 0:
                    if stack[-1] < abs(asteroid):  # Right-moving asteroid is smaller
                        stack.pop()  # Destroy right-moving asteroid, keep checking
                    elif stack[-1] == abs(asteroid):  # Both are equal, destroy both
                        stack.pop()
                        break
                    else:  # Right-moving asteroid is bigger, destroy current asteroid
                        break
                else:
                    # If no right-moving asteroid is left, push the left-moving one
                    stack.append(asteroid)

        return stack
            