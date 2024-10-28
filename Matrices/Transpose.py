class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose=[]
        for j in range(0,len(matrix[0])):
            temp=[]
            for i in range(0,len(matrix)):
                temp.append(matrix[i][j])
            transpose.append(temp)
            temp=[]
        return transpose