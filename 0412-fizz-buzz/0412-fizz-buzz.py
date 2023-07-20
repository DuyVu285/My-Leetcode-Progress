class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        word_list = ["FizzBuzz","Fizz","Buzz"]
        result = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append(word_list[0])
            elif i % 3 == 0:
                result.append(word_list[1])
            elif i % 5 == 0:
                result.append(word_list[2])
            else:
                result.append(str(i))
        
        return result