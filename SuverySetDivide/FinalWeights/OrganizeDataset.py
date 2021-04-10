import pandas as pd


class OrganizeData():
    def __init__(self):

        print("organizing data")

    def organizeData(self):
        answers1 = ['SET_NUM', 'GENDER', 'AGE_RANGE', 'OCCUPATION', 'FIELD_OF_EDUCATION', 'HOMETOWN', 'MARITAL_STATUS',
                    'SPOUSE_WILLING', 'SPOUSE_OCCUPATION', 'PREF_RENT', 'PREF_HOMETOWN', 'PREF_SCHOOL', 'PREF_SPOUSE',
                    'PREF_SECURITY', 'ANSWER_1']
        answers2 = ['SET_NUM', 'GENDER', 'AGE_RANGE', 'OCCUPATION', 'FIELD_OF_EDUCATION', 'HOMETOWN', 'MARITAL_STATUS',
                    'SPOUSE_WILLING', 'SPOUSE_OCCUPATION', 'PREF_RENT', 'PREF_HOMETOWN', 'PREF_SCHOOL', 'PREF_SPOUSE',
                    'PREF_SECURITY', 'ANSWER_2']
        answers3 = ['SET_NUM', 'GENDER', 'AGE_RANGE', 'OCCUPATION', 'FIELD_OF_EDUCATION', 'HOMETOWN', 'MARITAL_STATUS',
                    'SPOUSE_WILLING', 'SPOUSE_OCCUPATION', 'PREF_RENT', 'PREF_HOMETOWN', 'PREF_SCHOOL', 'PREF_SPOUSE',
                    'PREF_SECURITY', 'ANSWER_3']
        questionnaire1 = ['SET_NUM', 'QUESTION_1_SECURITY', 'QUESTION_1_SCHOOL', 'QUESTION_1_RENT', 'QUESTION_1_DISTANCE']
        questionnaire2 = ['SET_NUM', 'QUESTION_2_SECURITY', 'QUESTION_2_SCHOOL', 'QUESTION_2_RENT',
                          'QUESTION_2_DISTANCE']
        questionnaire3 = ['SET_NUM', 'QUESTION_3_SECURITY', 'QUESTION_3_SCHOOL', 'QUESTION_3_RENT',
                          'QUESTION_3_DISTANCE']

        df1 = pd.read_csv("Query main.csv", usecols=answers1)
        df2 = pd.read_csv("Query main.csv", usecols=answers2)
        df3 = pd.read_csv("Query main.csv", usecols=answers3)

        questionnaire1 = pd.read_csv("Questionnaire.csv", usecols=questionnaire1)
        questionnaire2 = pd.read_csv("Questionnaire.csv", usecols=questionnaire2)
        questionnaire3 = pd.read_csv("Questionnaire.csv", usecols=questionnaire3)
        df2 = df2.rename(columns={'ANSWER_2': 'ANSWER_1'})
        df3 = df3.rename(columns={'ANSWER_3': 'ANSWER_1'})

        questionnaire1 = questionnaire1.rename(columns={'QUESTION_1_SECURITY':'SECURITY', 'QUESTION_1_SCHOOL':'SCHOOL', 'QUESTION_1_RENT':'RENT', 'QUESTION_1_DISTANCE':'DISTANCE'})
        questionnaire2 = questionnaire2.rename(
            columns={'QUESTION_2_SECURITY': 'SECURITY', 'QUESTION_2_SCHOOL': 'SCHOOL', 'QUESTION_2_RENT': 'RENT',
                     'QUESTION_2_DISTANCE': 'DISTANCE'})
        questionnaire3 = questionnaire3.rename(
            columns={'QUESTION_3_SECURITY': 'SECURITY', 'QUESTION_3_SCHOOL': 'SCHOOL', 'QUESTION_3_RENT': 'RENT',
                     'QUESTION_3_DISTANCE': 'DISTANCE'})

        df1 = pd.merge(df1, questionnaire1, on=['SET_NUM', 'SET_NUM'])
        df2 = pd.merge(df2, questionnaire2, on=['SET_NUM', 'SET_NUM'])
        df3 = pd.merge(df3, questionnaire3, on=['SET_NUM', 'SET_NUM'])

        df1 = df1.append(df2)
        df1 = df1.append(df3)
        df1.to_csv("testing.csv", encoding='utf-8')