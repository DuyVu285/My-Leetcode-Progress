class Solution(object):
    def findRelativeRanks(self, scores):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        rank_dict = {}
        for i, score in enumerate(sorted(scores, reverse=True)):
             rank_dict[score] = i + 1

        answer = []
        for score in scores:
            rank = rank_dict[score]
            if rank == 1:
                answer.append("Gold Medal")
            elif rank == 2:
                answer.append("Silver Medal")
            elif rank == 3:
                answer.append("Bronze Medal")
            else:
                answer.append(str(rank))

        return answer