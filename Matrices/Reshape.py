class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (len(mat)* len(mat[0]))== r*c:
            flatten=[]
            for i in range(0,len(mat)):
                for j in range(0,len(mat[0])):
                    flatten.append(mat[i][j])
            new = [flatten[i:i + c] for i in range(0, len(flatten), c)] 
            return new
        else:
            return mat