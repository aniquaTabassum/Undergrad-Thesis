import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import Normalizer
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.compose import TransformedTargetRegressor
from sklearn.preprocessing import QuantileTransformer, quantile_transform, PolynomialFeatures
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.neural_network import MLPRegressor
import seaborn as sn

class FindWeight():
    def __init__(self):
        self.dataset = None
        self.X = None
        self.y = None
        self.mode = None
        self.cv_data = None
    def modify_dataset(self):
        self.dataset = pd.read_csv("testing.csv")
        self.dataset["AGE_RANGE"] = self.dataset["AGE_RANGE"].replace(
            ["20-25", "26-30", "31-35", "36-40", "41 or Above"],
            [20, 26, 31, 36, 41])
        self.dataset["GENDER"] = self.dataset["GENDER"].replace(["Male", "Female", "Prefer not to disclose"], [1, 2, 3])
        self.dataset["OCCUPATION"] = self.dataset["OCCUPATION"].replace(
            ["Medical Field (Doctor, Nurse, Nutritionist, Pharmacists and other Health Care workers etc)",
             "Engineering and IT",
             "Business Field (Management, HR, Banking, Marketing etc)",
             "Academia (Teacher, Lecturer, Assistant/ Associate Professor, Professor)", "Student", "Unemployed",
             "Other"], [1, 2, 3, 4, 5, 6, 7])
        self.dataset["FIELD_OF_EDUCATION"] = self.dataset["FIELD_OF_EDUCATION"].replace(
            ["Medical, Biological or Chemical studies",
             "Engineering and IT",
             "Business Field", "Social Studies", "Other"],
            [1, 2, 3, 4, 5])
        self.dataset["MARITAL_STATUS"] = self.dataset["MARITAL_STATUS"].replace(["Married", "Unmarried"], [1, 2])
        self.dataset["SPOUSE_WILLING"] = self.dataset["SPOUSE_WILLING"].replace(
            ["Yes", "No", "My Spouse Does Not Work", "I am not Married"], [1, 2, 3, 4])
        self.dataset["SPOUSE_OCCUPATION"] = self.dataset["SPOUSE_OCCUPATION"].replace(
            ["Medical Field (Doctor, Nurse, Nutritionist, Pharmacists and other Health Care workers etc)",
             "Engineering and IT",
             "Business Field (Management, HR, Banking, Marketing etc)",
             "Academia (Teacher, Lecturer, Assistant/ Associate Professor, Professor)", "Student", "Unemployed",
             "Other",
             "I am not Married"], [1, 2, 3, 4, 5, 6, 7, 8])

    def write_dataset(self):
        #self.X = self.dataset[['SECURITY', 'SCHOOL', 'RENT', 'DISTANCE']].values
        self.y = self.dataset['ANSWER_1'].values
        self.X = self.dataset[['GENDER', 'AGE_RANGE', 'OCCUPATION', 'FIELD_OF_EDUCATION', 'HOMETOWN', 'MARITAL_STATUS', 'SPOUSE_WILLING',
                                'SPOUSE_OCCUPATION', 'PREF_RENT', 'PREF_HOMETOWN', 'PREF_SCHOOL', 'PREF_SPOUSE', 'PREF_SECURITY',
                                'SECURITY', 'SCHOOL', 'RENT', 'DISTANCE']].values

        X_train, X_cross_and_test, y_train, y_cross_and_test = train_test_split(self.X, self.y, test_size=0.4, random_state=0)
        x_cross, x_test, y_cross, y_test = train_test_split(X_cross_and_test, y_cross_and_test, test_size=0.5,
                                                            random_state=0)
        train_to_write = pd.DataFrame(X_train)
        train_to_write['ANSWER1'] = y_train
        #train_to_write.to_csv(r'C:\Users\USER\Documents\AUST CSE 4.1\Undergrad Thesis\SuverySetDivide\FinalWeights\training_data_whole.csv', index=False, header=True)
        cv_to_write = pd.DataFrame(x_cross)
        cv_to_write['ANSWER'] = y_cross
        #cv_to_write.to_csv(r'C:\Users\USER\Documents\AUST CSE 4.1\Undergrad Thesis\SuverySetDivide\FinalWeights\cross_validation_data_whole.csv',index=False, header= True)

        test_to_write = pd.DataFrame(x_test)
        test_to_write['ANSWER'] = y_test
        test_to_write.to_csv(r'/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/FinalWeights/testing_dataset_whole.csv',index=False, header= True)
        print("finished")

    def weightCalculate(self):
        self.dataset = pd.read_csv("/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/FinalWeights/training_data_whole.csv" )
       # self.dataset = self.dataset[self.dataset['OCCUPATION'] == 7]
        #X_train = self.dataset[['SECURITY', 'SCHOOL', 'RENT', 'DISTANCE']].values
        X_train = self.dataset[['GENDER', 'AGE_RANGE',  'OCCUPATION',  'SECURITY', 'SCHOOL', 'RENT', 'DISTANCE']].values
        y_train = self.dataset['ANSWER1'].values

        self.dataset = pd.read_csv("/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/FinalWeights/cross_validation_data_whole.csv")

        #x_cross = self.dataset[['SECURITY', 'SCHOOL', 'RENT', 'DISTANCE']].values
        x_cross = self.dataset[['GENDER', 'AGE_RANGE', 'OCCUPATION',  'SECURITY', 'SCHOOL', 'RENT',  'DISTANCE']].values
        y_cross = self.dataset['ANSWER'].values
        scaler = StandardScaler().fit(X_train)
        scaler.transform(X_train)
        transformer = Normalizer().fit(X_train)
        transformer.transform(X_train)


        '''
        regressor_lr = TransformedTargetRegressor(regressor=LinearRegression(),
                                        func=np.log1p,
                                        inverse_func=np.expm1)
        #regressor = linear_model.Ridge(alpha=.5)
        #regressor = make_pipeline(StandardScaler(), SVR(kernel='linear',C=1.0, epsilon=0.2))
        #regressor = tree.DecisionTreeRegressor()
        regressor_rf = TransformedTargetRegressor(regressor=RandomForestRegressor(n_estimators=50), func=np.log1p, inverse_func=np.expm1)

        train_sizes = [1, 50, 200, 300, 400]

        train_sizes, train_scores, validation_scores = learning_curve(estimator=MLPRegressor(22, solver='lbfgs', random_state=1, max_iter= 900, alpha=0.0007), X = X_train,
                                                                      y = y_train, train_sizes = train_sizes, cv = 5, scoring= 'neg_mean_squared_error',
                                                                      shuffle= True)

        print('Training scores:\n\n', train_scores)
        print('\n', '-' * 70)  # separator to make the output easy to read
        print('\nValidation scores:\n\n', validation_scores)

        train_scores_mean = -train_scores.mean(axis=1)
        validation_scores_mean = -validation_scores.mean(axis=1)
        print('Mean training scores\n\n', pd.Series(train_scores_mean, index=train_sizes))
        print('\n', '-' * 20)  # separator
        print('\nMean validation scores\n\n', pd.Series(validation_scores_mean, index=train_sizes))

        plt.style.use('seaborn')
        plt.plot(train_sizes, train_scores_mean, label='Training error')
        plt.plot(train_sizes, validation_scores_mean, label='Validation error')
        plt.ylabel('MSE', fontsize=14)
        plt.xlabel('Training set size', fontsize=14)
        plt.title('Learning curves for a linear regression model', fontsize=18, y=1.03)
        plt.legend()
        plt.ylim(0, 10)
        #plt.show()

        regressor_rf.fit(X_train, y_train)
        regressor_lr.fit(X_train, y_train)

        y_pred_rf = regressor_rf.predict(x_cross)
        y_pred_lr = regressor_lr.predict(x_cross)

        print('Root Mean Squared Error Random forest:', np.sqrt(metrics.mean_squared_error(y_cross, y_pred_rf)))
        print('Root Mean Squared Error linear regression:', np.sqrt(metrics.mean_squared_error(y_cross, y_pred_lr)))
        print("RF score is "+str(regressor_rf.score(x_cross, y_cross)))
        print("LR score is " + str(regressor_lr.score(x_cross, y_cross)))
        print("   ")
        '''
        #clf = MLPRegressor(15, solver='lbfgs', random_state=1, max_iter= 1000, alpha=0.00013).fit(X_train, y_train)
        clf = MLPRegressor(hidden_layer_sizes=100, batch_size = 16, solver='lbfgs', random_state=1, max_iter=1000, alpha=0.00013).fit(X_train, y_train)
        y_pred_nn = clf.predict(x_cross)
        self.model = clf
        self.cv_data = x_cross
        #print('Root Mean Squared Error NN:', np.sqrt(metrics.mean_squared_error(y_cross, y_pred_nn)))
        #print(clf.score(x_cross, y_cross))

    def satisfaction_prediction(self, sample):
        y_pred_nn = self.model.predict(np.array(sample).reshape(1, -1))
        return np.round(y_pred_nn)