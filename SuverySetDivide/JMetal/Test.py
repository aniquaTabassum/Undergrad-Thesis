import random
from collections import Counter
class Dispersion():
    def __init__(self, list, min_allocation_list = [], demand_list = []):
        self.allocation_list = list
        self.min_allocation_list = min_allocation_list
        self.demand_list = demand_list
    def dispersion(self):
        nd = 0
        sum_demand_supply = 0
        for i in range(len(self.min_allocation_list)):
            allocation_in_city = list(filter(lambda x: x == i, self.allocation_list))
            len_of_area = len(allocation_in_city)
            if len_of_area >= self.min_allocation_list[i]:
                nd +=1
            demand_met = len_of_area/ self.demand_list[i]
            sum_demand_supply+=demand_met

        print("nd is ", nd," and demand met is ", sum_demand_supply)
        return nd+sum_demand_supply

class Repair():
    # here demand list refers to minimum requirement list for cities
    def __init__(self, min_requirement_list, supply_list, max_requirement_list = []):
        self.supply_tuple_list = []
        self.min_req_tuple_list = []
        self.max_req_tuple_list = []
        for i in range(len(supply_list)):
            self.supply_tuple_list.append([i, supply_list[i]])
            self.min_req_tuple_list.append([i, min_requirement_list[i]])
            self.max_req_tuple_list.append([i, max_requirement_list[i]])

    def repair(self):
        supply_min_req_zipped = list(zip(self.supply_tuple_list, self.min_req_tuple_list))
        filtered_list_shortage = [x[0] for x in list(filter(lambda x : x[0][1] < x[1][1], supply_min_req_zipped))]
        filtered_list_surplus = [x[0] for x in list(filter(lambda x: x[0][1] > x[1][1], supply_min_req_zipped))]
        filtered_list_equal = [x[0] for x in list(filter(lambda x: x[0][1] == x[1][1], supply_min_req_zipped))]
        print(supply_min_req_zipped)
        '''
        print("")
        print(filtered_list_equal)
        print(filtered_list_shortage)
        print(filtered_list_surplus)
        '''
        while len(filtered_list_shortage) != 0:
            random_city_to_increase = random.randint(0, len(filtered_list_shortage)-1)
            shortage_of_city = self.min_req_tuple_list[filtered_list_shortage[random_city_to_increase][0]][1] - self.supply_tuple_list[filtered_list_shortage[random_city_to_increase][0]][1]
            '''
            print(self.demand_tuple_list)
            print(self.supply_tuple_list)
            print(filtered_list_shortage)
            print("randomly picked ", random_city_to_increase, " index. shortage is ", shortage_of_city)
            '''

            random_city_to_decrease = random.randint(0, len(filtered_list_surplus) - 1)
            surplass_of_city = -1*(self.min_req_tuple_list[filtered_list_surplus[random_city_to_decrease][0]][1] - self.supply_tuple_list[filtered_list_surplus[random_city_to_decrease][0]][1])
            '''
            print(self.demand_tuple_list)
            print(self.supply_tuple_list)
            print(filtered_list_surplus)
            print("randomly picked ", random_city_to_decrease, " index. surplass is ", surplass_of_city)
            '''

            if surplass_of_city > shortage_of_city:
                self.supply_tuple_list[filtered_list_surplus[random_city_to_decrease][0]][1] = self.min_req_tuple_list[filtered_list_surplus[random_city_to_decrease][0]][1] + shortage_of_city
                self.supply_tuple_list[filtered_list_shortage[random_city_to_increase][0]][1] += (surplass_of_city - shortage_of_city)
            else:
                self.supply_tuple_list[filtered_list_surplus[random_city_to_decrease][0]][1] = self.min_req_tuple_list[filtered_list_surplus[random_city_to_decrease][0]][1]
                self.supply_tuple_list[filtered_list_shortage[random_city_to_increase][0]][1] += surplass_of_city

            filtered_list_shortage = [x[0] for x in list(filter(lambda x: x[0][1] < x[1][1], supply_min_req_zipped))]
            filtered_list_surplus = [x[0] for x in list(filter(lambda x: x[0][1] > x[1][1], supply_min_req_zipped))]
            filtered_list_equal = [x[0] for x in list(filter(lambda x: x[0][1] == x[1][1], supply_min_req_zipped))]
            '''
            print(filtered_list_equal)
            print(filtered_list_shortage)
            print(filtered_list_surplus)
            '''
        print("")
        print(supply_min_req_zipped)

        # fixing if any city has crossed maximum requirement
        print("")
        supply_max_zipped = list(zip(self.supply_tuple_list, self.max_req_tuple_list))
        print("supply-max zipped list")
        print(supply_max_zipped)
        over_supply_list = [x[0] for x in list(filter(lambda x: x[0][1] > x[1][1], supply_max_zipped))]
        saturated_list = [x[0] for x in list(filter(lambda x: x[0][1] == x[1][1], supply_max_zipped))]
        normal_supply_list = [x[0] for x in list(filter(lambda x: x[0][1] < x[1][1], supply_max_zipped))]
        print(over_supply_list)
        print(saturated_list)
        print(normal_supply_list)
        while(len(over_supply_list) != 0):
            random_city_to_decrease = random.randint(0, len(over_supply_list) - 1)
            surplass_of_city = -1*(self.max_req_tuple_list[over_supply_list[random_city_to_decrease][0]][1] - self.supply_tuple_list[over_supply_list[random_city_to_decrease][0]][1])
            random_city_to_increase = random.randint(0, len(normal_supply_list) - 1)
            shortage_of_city = self.max_req_tuple_list[normal_supply_list[random_city_to_increase][0]][1] - self.supply_tuple_list[normal_supply_list[random_city_to_increase][0]][1]
            if(surplass_of_city > shortage_of_city):
                self.supply_tuple_list[over_supply_list[random_city_to_decrease][0]][1] -= shortage_of_city
                self.supply_tuple_list[normal_supply_list[random_city_to_increase][0]][1] += shortage_of_city
            else:
                self.supply_tuple_list[over_supply_list[random_city_to_decrease][0]][1] -= surplass_of_city
                self.supply_tuple_list[normal_supply_list[random_city_to_increase][0]][1] += surplass_of_city

            over_supply_list = [x[0] for x in list(filter(lambda x: x[0][1] > x[1][1], supply_max_zipped))]
            saturated_list = [x[0] for x in list(filter(lambda x: x[0][1] == x[1][1], supply_max_zipped))]
            normal_supply_list = [x[0] for x in list(filter(lambda x: x[0][1] < x[1][1], supply_max_zipped))]

        print(supply_max_zipped)

class Custom_Mutation():
    def __init__(self, solution, probability, number_of_city, demand_list):
        self.solution = solution
        self.probability = probability
        self.number_of_city = number_of_city
        self.demand_list = demand_list
    def execute(self):

        random_probability = random.random()

        if random_probability <= self.probability:
            # Case 1
            if len(set(self.solution)) == self.number_of_city:
                random_index = random.randint(0, len(self.solution)-1)
                current_city = self.solution[random_index]
                random_city = current_city
                while random_city == current_city:
                    random_city = random.randint(0, self.number_of_city-1)
                self.solution[random_index] = random_city

            # Case 2
            else:
                most_allocated_city = Counter(self.solution).most_common(1)[0][0]
                set_of_unallocated_city = {i for i in range(self.number_of_city)}.symmetric_difference(set(self.solution))
                demand_list_for_unallocated_cities = []
                for d in set_of_unallocated_city:
                    demand_list_for_unallocated_cities.append((d, self.demand_list[d]))
                demand_list_for_unallocated_cities = sorted(demand_list_for_unallocated_cities, key = lambda x: x[1], reverse=True)
                doctor_list_in_most_allocated_city = [(idx, city)[0] for idx, city in enumerate(self.solution) if self.solution[idx] == most_allocated_city]
                random_index = random.randint(0, len(doctor_list_in_most_allocated_city)-1)
                random_index = doctor_list_in_most_allocated_city[random_index]
                self.solution[random_index] = demand_list_for_unallocated_cities[0][0]
            print(self.solution)








'''
d = Dispersion([0, 1, 2, 0, 0, 5, 1, 0, 1, 5, 0, 5, 1, 0, 4, 3, 0, 0, 1, 3, 1, 3, 0, 5, 1, 0, 1, 4, 0, 2, 0, 0, 0, 4, 2, 4], [3, 3, 3, 2, 2, 2, 2], [6, 6, 6, 5, 5, 4, 4])
dispersion = d.dispersion()
print(dispersion)



repair_var = Repair([3, 3, 3, 2, 2, 2, 2], [9, 2, 6, 2, 1, 1, 1], max_requirement_list=[6, 2, 5, 3, 2, 3, 5])
repair_var.repair()

'''

custom_mutation = Custom_Mutation(solution=[0, 1, 2, 3, 4, 4, 6, 5, 5, 2], probability=1.0, number_of_city=7, demand_list=[2, 1, 1, 1, 1, 1, 1])
custom_mutation.execute()