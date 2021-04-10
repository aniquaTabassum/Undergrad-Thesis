from FinalWeights import OrganizeDataset
from FinalWeights import LinearRegression


regression_with_cv = LinearRegression.FindWeight()
regression_with_cv.weightCalculate()
s = regression_with_cv.satisfaction_prediction([2, 20, 1, 3, 3, 3, 3])
print(s[0])

#reg = LinearRegression.FindWeight()
#reg.modify_dataset()
#reg.write_dataset()


