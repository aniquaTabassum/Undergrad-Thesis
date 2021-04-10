# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting
multiplicaton_factor = 1
def recDet(matrix):
   global multiplication_factor
   sum = 0;
   if len(matrix[0]) == 1:
       sum += multiplication_factor * matrix[0][0]
       print("sum is "+str(sum))
       return sum

   for i in range(len(matrix[0])):
       if i%2 == 0:
           multiplication_factor = matrix[0][i]
       else:
           multiplication_factor = (-1) * matrix[0][i]
       new_matrix = [[0 for t in range(len(matrix[0]) - 1)] for t in range(len(matrix) - 1)]
       for j in range(1, len(matrix[0])):
           l = 0
           for k in range(len(matrix[0])):
                if k == i:
                    continue
                new_matrix[j-1][l] = matrix[j][k]
                l += 1
       print(new_matrix)
       recDet(new_matrix)



recDet([[1,2,3], [4,5,6], [7,8,9]])
