class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or n <= numRows:
            return s
        
        rows = ['']* numRows
        
        currentRow = 0
        goingDown = False
        
        for char in s:
            rows[currentRow] += char
            
            if currentRow == 0 or currentRow == numRows -1:
                goingDown = not goingDown
            
            currentRow += 1 if goingDown else -1
            
        return ''.join(rows)
        
        
        
        
        