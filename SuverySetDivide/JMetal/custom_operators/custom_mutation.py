import random
from collections import Counter
from jmetal.core.operator import Mutation
from jmetal.core.solution import BinarySolution, Solution, FloatSolution, IntegerSolution, PermutationSolution, \
    CompositeSolution
from jmetal.util.ckecking import Check


class Domain_Knowledge_mutation(Mutation[IntegerSolution]):

    def __init__(self, number_of_city, demand_list, probability: float, weights, doctors, areas, num_of_variables):
        super(Domain_Knowledge_mutation, self).__init__(probability=probability)
        self.number_of_city = number_of_city
        self.demand_list = demand_list
        self.weights = weights
        self.doctors = doctors
        self.areas = areas
        self.num_of_variables = num_of_variables

    def execute(self, solution: IntegerSolution) -> IntegerSolution:
        Check.that(issubclass(type(solution), IntegerSolution), "Solution type invalid")
        random_probability = random.random()
        satisfaction_or_dispersion_probability = random.random()()
        if random_probability <= self.probability:
            if satisfaction_or_dispersion_probability <= 0.5:
                city_to_reallocate_and_by_whom = self.balance_dispersion(solution)
                # Replace city of randomly chosen doctor with the city with the highest demand from unallocated cities
                solution.variables[city_to_reallocate_and_by_whom[0]] = city_to_reallocate_and_by_whom[1]
                # solution.variables[doctor_to_allocate] = unallocated_city_with_most_demand

            else:
                doctor_to_and_where_to_allocate = self.increase_satisfaction_of_a_doctor()
                solution.variables[doctor_to_and_where_to_allocate[0]] = doctor_to_and_where_to_allocate[1]

        return solution

    def balance_dispersion(self, solution):
        # Case 1
        if len(set(solution.variables)) == self.number_of_city:
            random_index = random.randint(0, len(solution.variables) - 1)
            current_city = solution.variables[random_index]
            random_city = current_city
            while random_city == current_city:
                random_city = random.randint(0, self.number_of_city - 1)
            solution.variables[random_index] = random_city

        # Case 2
        else:
            # Find the city with highest allocation
            most_allocated_city = Counter(solution.variables).most_common(1)[0][0]
            # Find the cities with 0 allocation
            set_of_unallocated_city = {i for i in range(self.number_of_city)}.symmetric_difference(
                set(solution.variables))
            demand_list_for_unallocated_cities = []
            # Find and sort demands for the cities with 0 allocation
            for d in set_of_unallocated_city:
                demand_list_for_unallocated_cities.append((d, self.demand_list[d]))
            demand_list_for_unallocated_cities = sorted(demand_list_for_unallocated_cities, key=lambda x: x[1],
                                                        reverse=True)

            # Find which doctors are allocated in the city with the most allocation
            doctor_list_in_most_allocated_city = [(idx, city)[0] for idx, city in enumerate(solution.variables)
                                                  if
                                                  solution.variables[idx] == most_allocated_city]

            unallocated_city_with_most_demand = demand_list_for_unallocated_cities[0][0]

            # Randomly choose a doctor that has been alocated in the city with the most allocation
            random_index = random.randint(0, len(doctor_list_in_most_allocated_city) - 1)
            random_index = doctor_list_in_most_allocated_city[random_index]

            return [random_index, unallocated_city_with_most_demand]

    def increase_satisfaction_of_a_doctor(self):
        random_doctor_to_satisfy = random.randint(0, self.num_of_variables - 1)
        city_to_allocate = -1
        current_doctor = self.doctors.doctor_dataset.iloc[random_doctor_to_satisfy]
        doctor_info = current_doctor.iloc[0:3].to_list()
        distant_list_from_curr_HT = list(self.areas.distances_dict[current_doctor.iloc[3]].values())
        for i in range(self.number_of_city):
            area_info = self.areas.area_dataset.iloc[i, :].to_list()
            parameter_of_NN = [doctor_info[0], doctor_info[1], doctor_info[2], area_info[2], area_info[1], area_info[0],
                               distant_list_from_curr_HT[i]]
            satisfaction_in_area = self.weights.satisfaction_prediction(parameter_of_NN)
            if satisfaction_in_area[0] > most_satisfaction:
                city_to_allocate = i
                most_satisfaction = satisfaction_in_area[0]

            if satisfaction_in_area[0] == most_satisfaction:
                should_change_doctor = random.randint(0, 1)
                if should_change_doctor == 1:
                    city_to_allocate = i
                    most_satisfaction = satisfaction_in_area[0]

        return [random_doctor_to_satisfy, city_to_allocate]

    def get_name(self):
        return 'Domain Knowledge Mutation (Integer)'


class Random_Integer_Mutation(Mutation[IntegerSolution]):

    def __init__(self, number_of_city, probability: float):
        super(Random_Integer_Mutation, self).__init__(probability=probability)
        self.number_of_city = number_of_city

    def execute(self, solution: IntegerSolution) -> IntegerSolution:
        Check.that(issubclass(type(solution), IntegerSolution), "Solution type invalid")
        random_probability = random.random()

        if random_probability <= self.probability:
            random_index = random.randint(0, len(solution.variables) - 1)
            current_city = solution.variables[random_index]
            random_city = current_city
            while random_city == current_city:
                random_city = random.randint(0, self.number_of_city - 1)
            solution.variables[random_index] = random_city

        return solution

    def get_name(self):
        return 'Simple Random Mutation (Integer)'
