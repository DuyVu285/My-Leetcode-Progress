class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                
                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                sub_box_index = (r//3)* 3 + (c//3)
                if num in sub_boxes[sub_box_index]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                sub_boxes[sub_box_index].add(num)
                
        return True
