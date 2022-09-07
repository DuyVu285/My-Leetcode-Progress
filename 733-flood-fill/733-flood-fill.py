class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])
        orig_color = image[sr][sc]
        def traverse(row,col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:
                return
            image[row][col] = color
            [traverse(row + x,col + y) for (x,y) in ((0,1),(1,0),(-1,0),(0,-1))]
        if orig_color != color:
            traverse(sr,sc)
        return image
        