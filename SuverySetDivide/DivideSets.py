import random


def first_column():
    inital_list = [0, 1, 2]
    return [t for k in range(27) for t in inital_list]


def second_column():
    initial_list = [0, 1, 2]
    return [t for k in range(9) for t in initial_list for j in range(3)]


def third_column():
    initial_list = [0, 1, 2]
    return [t for k in range(3) for t in initial_list for j in range(9)]


def fourth_column():
    initial_list = [0, 1, 2]
    return [t for t in initial_list for j in range(27)]


def create_questionnaire_sets(all_combination_list, number_of_partition):
    questionnaire_set = [[] for k in range(number_of_partition)]
    number_of_iteration = len(all_combination_list[0]) // number_of_partition
    index = 0
    temp = [[a, b, c, d] for a, b, c, d in
            zip(all_combination_list[0], all_combination_list[1], all_combination_list[2],
                all_combination_list[3])]

    for i in range(number_of_iteration):
        for j in range(number_of_partition):
            if len(temp) == 1:
                index = 0
            else:
                index = random.randint(0, len(temp) - 1)
            questionnaire_set[j].append(temp[index])
            temp.pop(index)
    return questionnaire_set


def create_file(questionnaire):
    name_of_files = []
    for i in range(len(questionnaire)):
        name = "Questionnaire " + str(i + 1)
        name_of_files.append(name)
    for i in range(len(questionnaire)):
        f = open(name_of_files[i], "w")
        for j in range(len(questionnaire[i])):
            toWrite = ""
            for k in range(len(questionnaire[i][j])):
                if questionnaire[i][j][k] == 0:
                    toWrite += "Low "
                elif questionnaire[i][j][k] == 1:
                    toWrite += "Medium "
                else:
                    toWrite += "High "
                if k == 0:
                    toWrite += "Security, "
                elif k == 1:
                    toWrite += "Schooling, "
                elif k == 2:
                    toWrite += "House Rent, "
                else:
                    toWrite += "Distance from hometown "

            f.writelines(str(j+1)+". "+toWrite + "\n")
        f.close()


first_column_list = first_column()
second_column_list = second_column()
third_column_list = third_column()
fourth_column_list = fourth_column()
questionnaire_set = create_questionnaire_sets(
    [first_column_list, second_column_list, third_column_list, fourth_column_list], 9)
for i in range(len(questionnaire_set)):
    for j in range(len(questionnaire_set[i])):
        print(questionnaire_set[i][j])
    print(len(questionnaire_set[i]))
    print()
create_file(questionnaire_set)
