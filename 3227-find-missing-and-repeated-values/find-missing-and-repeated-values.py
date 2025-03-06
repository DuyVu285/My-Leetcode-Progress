class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        flat_list = [item for row in grid for item in row]
        unique = set(flat_list)
        counter = Counter(flat_list)
        most_common_key = max(counter, key=counter.get)
        result = [most_common_key]
        for i in range(1,len(flat_list)+1):
            if i not in unique:
                result.append(i)
        return result