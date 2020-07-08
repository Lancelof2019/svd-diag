import numpy as np
matrix_test=np.array([[1,2,3],[3,4,5],[5,6,7]])

print(matrix_test)

print("#######################")
print(matrix_test[:,2])
print("#######################")
print(matrix_test[1:3])
print(matrix_test[2:3])

print(matrix_test[0:3])
print(matrix_test[0:2])
print("**********")
print(matrix_test[1:,2])

print(matrix_test[0:,1])

print(matrix_test[0:3,2])
print(matrix_test[0:2,1:3])
###############################
U,S,V=np.linalg.svd(matrix_test)
##############################

print(S)


print(np.mat(np.diag(S)))
