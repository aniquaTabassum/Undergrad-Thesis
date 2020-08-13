from methodology import Female
from methodology import Male
import numpy as np
import matplotlib.pyplot as plt
import random
import csv

noise_index = 0
age_list = ["20 - 25", "26 - 30", "31 - 35", "36 - 40", "41 or above"]
gender_list = ["male", "female", "prefer not to disclose"]
occupation_list = ["Medical", "Engineering and IT", "Business", "Academia", "Student", "Other"]
education_list = ["Medical, Biological, Chemical", "Engineering", "Business", "Social", "Science", "Other"]
district_list = ["Barguna", "Barisal", "Bhola", "Jhalokati", "Patuakhali", "Pirojpur", "Bandarban", "Brahmanbaria",
                 "Chandpur", "Chittagong", "Comilla",
                 "Cox's Bazar", "Feni", "Khagrachhari", "Lakshmipur", "Noakhali", "Rangamati", "Dhaka", "Faridpur",
                 "Gazipur", "Gopalganj", "Kishoreganj",
                 "Madaripur", "Manikganj", "Munshiganj", "Narayanganj", "Narsingdi", "Rajbari", "Shariatpur", "Tangail",
                 "Bagerhat", "Chuadanga", "Jessore",
                 "Jhenaidah", "Khulna", "Kushtia", "Magura", "Meherpur", "Narail", "Satkhira", "Jamalpur", "Mymensingh",
                 "Netrokona", "Sherpur",
                 "Bogra", "Joypurhat", "Naogaon", "Natore", "Chapainawabganj", "Pabna", "Rajshahi", "Sirajganj",
                 "Dinajpur",
                 "Gaibandha", "Kurigram", "Lalmonirhat",
                 "Nilphamari", "Panchagarh", "Rangpur", "Thakurgaon", "Habiganj", "Moulvibazar", "Sunamganj", "Sylhet"]

marital_status_list = ["Married", "Unmarried"]
spouse_moving_status_list = ["Yes", "No", "Spouce does not work", "not married"]

spouse_working_status_list = ["Medical, Biological, Chemical", "Engineering", "Business", "Social", "Science", "Other",
                              "I am not married", "Spouse does not work"]

noise = []


def select_age_range():
    return random.randint(0, 4)


def select_gender():
    return random.randint(0, 2)


def select_occupation():
    return random.randint(0, 5)


def select_field_of_education():
    # leaving out Medical and IT field, as these two options will be assigned based on their occupation_list
    # since a doctor or an engineer cannot be those if they do not study in Medical or Engineering field consecutively
    # so, if they choose that they are doctors/engineers, then their fields will be assigned accordingly
    # in real surveys, some inconsistency may be seen in this question, which must be cleaned before proceeding
    return random.randint(2, 4)


def select_hometown():
    district_name = district_list[random.randint(0, 63)]
    upazilla = random.randint(1, 492)
    return district_name + "," + str(upazilla)


def select_marital_status():
    return random.randint(0, 1)


def select_spouse_moving_status():
    return random.randint(0, 2)


def select_spouse_working_status():
    return random.randint(0, 5)


def create_gender_object(gender_of_object):
    person = None
    global noise_index
    satisfaction_and_coeff_list = []
    coeff_list = []
    satisfaction_list = []
    if gender_of_object == "prefer not to disclose":
        gender_of_object = gender_list[random.randint(0, 1)]
    if gender_of_object == "female":
        person = Female.Female(marital_status_index, spouse_moving_status_index, spouse_working_status_index)
    else:
        person = Male.Male(marital_status_index, spouse_moving_status_index, spouse_working_status_index)
    for i in range(3):
        security_index = random.randint(0, 2)
        schooling_index = random.randint(0, 2)
        house_rent_index = random.randint(0, 2)
        distance_from_HT_index = random.randint(0, 2)
        temp_coeff = [person.security_levels_list[security_index], person.schooling_levels_list[schooling_index], person.house_rent_levels_list[house_rent_index], person.distance_from_HT_levels_list[distance_from_HT_index]]
        coeff_list.append(temp_coeff)
        satisfaction = person.satisfaction_function(security_index, schooling_index, house_rent_index,
                                                    distance_from_HT_index)
        satisfaction += noise[noise_index]
        noise_index += 1
        if satisfaction > 5.0:
            satisfaction = 5.0
        elif satisfaction < 0.0:
            satisfaction = 0.0
        satisfaction_list.append(round(satisfaction, 0))
    satisfaction_and_coeff_list.append(satisfaction_list)
    satisfaction_and_coeff_list.append(coeff_list)
    return satisfaction_and_coeff_list


def create_gaussian_noise():
    global noise
    noise = np.random.uniform(1, 0.5, 4000)


def write_in_csv_file(age, gender, occupation, field_of_education, hometown, marital_staus, spouse_moving_status,
                      spouse_working_status, satisfaction_values, coeff_list):

    filename = "dataset.csv"
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in range(3):
            row = [age, gender, occupation, field_of_education, hometown, marital_staus, spouse_moving_status,
                   spouse_working_status,coeff_list[i][0], coeff_list[i][1], coeff_list[i][2], coeff_list[i][3], satisfaction_values[i]]
            csvwriter.writerow(row)


create_gaussian_noise()
fields = ["age", "gender", "occupation", "education", "hometown", "marital status", "spouse moving status",
          "spouse employment status", "security", "schooling", "house rent", "distance from HT", "satisfaction"]
filename = "dataset.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvfile.close()
for i in range(1001):
    age_range = age_list[select_age_range()]
    gender = gender_list[select_gender()]
    occupation_index = select_occupation()
    occupation = occupation_list[occupation_index]

    field_of_education_index = 0
    if occupation_index == 1:
        field_of_education_index = 1
    elif occupation_index != 0 and occupation_index != 1:
        field_of_education_index = select_field_of_education()
    field_of_education = education_list[field_of_education_index]

    hometown = select_hometown()
    marital_status_index = select_marital_status()
    marital_status = marital_status_list[marital_status_index]

    spouse_moving_status_index = 3
    if marital_status_index == 0:
        spouse_moving_status_index = select_spouse_moving_status()
    spouse_moving_status = spouse_moving_status_list[spouse_moving_status_index]

    spouse_working_status_index = 6
    if marital_status_index == 0:
        spouse_working_status_index = select_spouse_working_status()
    spouse_working_status = spouse_working_status_list[spouse_working_status_index]
    satisfaction_and_coeff_list = create_gender_object(gender)
    write_in_csv_file(age_range, gender, occupation, field_of_education, hometown, marital_status, spouse_moving_status,
                      spouse_working_status, satisfaction_and_coeff_list[0], satisfaction_and_coeff_list[1])
