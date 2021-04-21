import random
from collections import Counter
from jmetal.core.operator import Mutation
from jmetal.core.solution import BinarySolution, Solution, FloatSolution, IntegerSolution, PermutationSolution, \
    CompositeSolution
from jmetal.util.ckecking import Check


class Domain_Knowledge_mutation(Mutation[IntegerSolution]):

    def __init__(self, number_of_city, demand_list, probability: float, weights, doctors, areas, num_of_variables, dream_allocation):
        super(Domain_Knowledge_mutation, self).__init__(probability=probability)
        self.number_of_city = number_of_city
        self.demand_list = demand_list
        self.weights = weights
        self.doctors = doctors
        self.areas = areas
        self.num_of_variables = num_of_variables
        self.dream_allocation = dream_allocation
    def execute(self, solution: IntegerSolution) -> IntegerSolution:
        Check.that(issubclass(type(solution), IntegerSolution), "Solution type invalid")
        random_probability = random.random()
        satisfaction_or_dispersion_probability = random.random()
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
            return [random_index, random_city]

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

        return [random_doctor_to_satisfy, self.dream_allocation[random_doctor_to_satisfy]]

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
