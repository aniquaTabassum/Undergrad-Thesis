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


def create_partition(first_digit, total_combination):
    return [t for t in total_combination if t[0] == first_digit]


def create_random_questionsets(total_combinations, num_of_sets):
    first_partition = create_partition(0, total_combinations)
    second_partition = create_partition(1, total_combinations)
    third_partition = create_partition(2, total_combinations)
    questionnaire_sets = [[] for k in range(num_of_sets)]

    for i in range(num_of_sets):
        index = random.randint(0, len(first_partition) - 1)
        questionnaire_sets[i].append(first_partition[index])
        second_question_index = find_question(second_partition, index, first_partition[index])
        first_partition.pop(index)
        questionnaire_sets[i].append(second_partition[second_question_index])
        third_question_index = find_question(third_partition, second_question_index, second_partition[second_question_index])
        second_partition.pop(second_question_index)
        questionnaire_sets[i].append(third_partition[third_question_index])
    return questionnaire_sets


def find_question(list, previous_question_index, previous_question):
    current_question_index = 0
    while abs(list[current_question_index][1] - previous_question[1]) + abs(list[current_question_index][2] - previous_question[2]) + abs(list[current_question_index][3] - previous_question[3]) < 2 and current_question_index == previous_question_index:
        current_question_index = random.randint(0, len(list) - 1)
    return current_question_index


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

            f.writelines(str(j + 1) + ". " + toWrite + "\n")
        f.close()


first_column_list = first_column()
second_column_list = second_column()
third_column_list = third_column()
fourth_column_list = fourth_column()

all_combination = [[a,b,c,d] for a,b,c,d in zip(fourth_column_list, third_column_list, second_column_list, first_column_list)]
questionnaire_set = create_random_questionsets(all_combination,27)

for i in range(len(questionnaire_set)):
    for j in range(len(questionnaire_set[i])):
        print(questionnaire_set[i][j], end=" ")
    print()
    print(len(questionnaire_set[i]))

create_file(questionnaire_set)