import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import HuberRegressor
from sklearn import metrics
from sklearn.metrics import r2_score


class FindWeight():
    def __init__(self):
        self.dataset = None

    def import_dataset(self):
        self.dataset = pd.read_csv("dataset.csv")
        self.dataset["AGE_RANGE"] = self.dataset["AGE_RANGE"].replace(["20 - 25", "26 - 30", "31 - 35", "36 - 40", "41 or above"],
                                                          [20, 26, 31, 36, 41])
        self.dataset["GENDER"] = self.dataset["GENDER"].replace(["male", "female", "prefer not to disclose"], [1, 2, 3])
        self.dataset["OCCUPATION"] = self.dataset["OCCUPATION"].replace(
            ["Medical", "Engineering and IT", "Business", "Academia", "Student", "Other"], [1, 2, 3, 4, 5, 6])
        self.dataset["FIELD_OF_EDUCATION"] = self.dataset["FIELD_OF_EDUCATION"].replace(
            ["Medical, Biological, Chemical", "Engineering", "Business", "Social", "Science", "Other"],
            [1, 2, 3, 4, 5, 6])
        self.dataset["MARITAL_STATUS"] = self.dataset["MARITAL_STATUS"].replace(["Married", "Unmarried"], [1, 2])
        self.dataset["spouse moving status"] = self.dataset["spouse moving status"].replace(
            ["Yes", "No", "Spouce does not work", "not married"], [1, 2, 3, 4])
        self.dataset["spouse employment status"] = self.dataset["spouse employment status"].replace(
            ["Medical, Biological, Chemical", "Engineering", "Business", "Social", "Science", "Other",
             "I am not married", "Spouse does not work"], [1, 2, 3, 4, 5, 6, 7, 8])

        X = self.dataset[['security', 'schooling', 'house rent', 'distance from HT']].values
        y = self.dataset['satisfaction'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        coeff_df = pd.DataFrame(regressor.coef_, ['security', 'schooling', 'house rent', 'distance from HT'],
                                columns=['Coefficient'])
        y_pred = regressor.predict(X_test)
        df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
        print(df.head(100))

        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        print("R2 score is ", r2_score(y_test, y_pred))

fw = FindWeight()
fw.import_dataset()