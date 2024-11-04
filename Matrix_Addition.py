def Matrix_Addition(Matrix1,Matrix2):
    result=[]
    for i in range (len(Matrix1)):
        row=[]
        for j in range(len(Matrix1[0])):
            row.append(Matrix1[i][j]+Matrix2[i][j])
        result.append(row)
    return result


Matrix1=[[1,2,3],[3,4,5],[6,7,8]]
Matrix2=[[1,2,3],[4,5,6],[7,8,9]]
Result_Matrix=Matrix_Addition(Matrix1,Matrix2)
print("Matrix Addition is:", Result_Matrix)
