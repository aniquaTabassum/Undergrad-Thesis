import random


def create_first_column():
    inital_list = [0, 1, 2]
    return [t for k in range(27) for t in inital_list]


def create_second_column():
    initial_list = [0, 1, 2]
    return [t for k in range(9) for t in initial_list for j in range(3)]


def create_third_column():
    initial_list = [0, 1, 2]
    return [t for k in range(3) for t in initial_list for j in range(9)]


def create_fourth_column():
    initial_list = [0, 1, 2]
    return [t for t in initial_list for j in range(27)]


# this function is responsible for the initial partition of the total_combination current_partition_list
# it will divide the current_partition_list based on the levels of the leftmost variable
# level 0, 1 and 2 will be partitioned into separate lists
# this will initially ensure the variation between two consequent question for the leftmost variable
def create_partition(first_digit, total_combination):
    return [t for t in total_combination if t[0] == first_digit]


def create_random_questionsets(total_combinations, num_of_sets):
    num_of_questions_per_set = len(total_combinations) / num_of_sets
    partitions = [[] for k in range(int(num_of_questions_per_set))]
    partitions[0] = create_partition(0, total_combinations)
    partitions[1] = create_partition(1, total_combinations)
    partitions[2] = create_partition(2, total_combinations)
    questionnaire_sets = [[] for k in range(num_of_sets)]

    index = 0
    for i in range(num_of_sets):
        for j in range(int(num_of_questions_per_set)):
            if j == 0:
                index = random.randint(0, len(partitions[0]) - 1)
                questionnaire_sets[i].append(partitions[0][index])
            else:
                current_question_index = find_question(partitions[j], index, partitions[j-1][index])
                partitions[j-1].pop(index)
                questionnaire_sets[i].append(partitions[j][current_question_index])
                index = current_question_index

    return questionnaire_sets


# this method is responsible for making sure that, after the initial variation
# created by the create_partition( ) method, at least one other variable's level
# between two questions are varying, creating more variation between two consecutive questions as a whole
def find_question(current_partition_list, previous_question_index, previous_question):
    current_question_index = random.randint(0, len(current_partition_list) - 1)
    while abs(current_partition_list[current_question_index][1] - previous_question[1]) + abs(current_partition_list[current_question_index][2] - previous_question[2]) + abs(current_partition_list[current_question_index][3] - previous_question[3]) < 3:
        current_question_index = random.randint(0, len(current_partition_list) - 1)
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


first_column_list = create_first_column()
second_column_list = create_second_column()
third_column_list = create_third_column()
fourth_column_list = create_fourth_column()

all_combination = [[a,b,c,d] for a,b,c,d in zip(fourth_column_list, third_column_list, second_column_list, first_column_list)]
questionnaire_set = create_random_questionsets(all_combination,27)

for i in range(len(questionnaire_set)):
    for j in range(len(questionnaire_set[i])):
        print(questionnaire_set[i][j], end=" ")
    print()
    print(len(questionnaire_set[i]))

create_file(questionnaire_set)