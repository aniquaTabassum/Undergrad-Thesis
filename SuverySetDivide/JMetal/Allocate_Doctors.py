from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.operator import SBXCrossover, PolynomialMutation
from jmetal.problem import DTLZ2
from jmetal.util.comparator import DominanceComparator
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file, read_solutions, \
    get_non_dominated_solutions
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.lab.visualization import Plot
import pandas as pd
import numpy as np
from jmetal.algorithm.multiobjective import NSGAII
from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.core.problem import FloatProblem, IntegerProblem
from jmetal.core.solution import FloatSolution, IntegerSolution
from jmetal.operator import BinaryTournamentSelection, PolynomialMutation, SBXCrossover
from jmetal.operator.mutation import Domain_Knowledge_mutation, IntegerPolynomialMutation, Random_Integer_Mutation
from jmetal.operator.crossover import IntegerSBXCrossover, IntegerSinglePointCrossover, IntegerMultiPointCrossover
from jmetal.problem.singleobjective.unconstrained import Rastrigin
from jmetal.util.comparator import DominanceComparator
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations
import math
from FinalWeights import LinearRegression

class Find_Optimum_Allocation(IntegerProblem):

    def __init__(self, number_of_variables: int = 2, number_of_city = 7, demand_list = []):
        super(Find_Optimum_Allocation, self).__init__()
        self.number_of_city = number_of_city
        self.doctors = Doctors("doctor_dataset.csv")
        self.doctors.extract_doctor_info()
        self.doctors.doctor_dataset = self.doctors.doctor_dataset[0:number_of_variables]
        self.areas = Areas("/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/merged.csv",
                      "/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/distances.csv")
        self.areas.categorize_schooling()
        self.areas.categorize_house_rent()
        self.areas.categorize_security()
        self.areas.create_distance_dict()
        self.areas.area_dataset = self.areas.area_dataset.set_index('City')

        self.NN_predictor = LinearRegression.FindWeight()
        self.NN_predictor.weightCalculate()
        self.number_of_objectives = 2
        self.number_of_variables = number_of_variables
        self.number_of_constraints = 0

        self.obj_directions = [self.MINIMIZE, self.MINIMIZE]
        self.obj_labels = ['satisfaction(x)', 'Dispersion']

        self.lower_bound = [0 for _ in range(number_of_variables)]
        self.upper_bound = [number_of_city-1 for _ in range(number_of_variables)]
        self.demand_list = demand_list
        self.min_allocation_list = []
        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound
        percent_of_doctor_available_list = []
        for i in range(number_of_city):
            percent_of_doctor_available_list.append((demand_list[i]/sum(demand_list))*100)


        for i in range(number_of_city):
            temp = (number_of_variables * percent_of_doctor_available_list[i])/100
            if(math.ceil(temp) - temp) > 0.5:
                self.min_allocation_list.append(math.floor(temp))
            else:
                self.min_allocation_list.append(math.ceil(temp))


        print(self.min_allocation_list)


    def evaluate(self, solution: IntegerSolution) -> IntegerSolution:

        x = solution.variables
        satisfaction_of_all_doctors = []
        #print(x)
        sum = 0

        for i in range(self.number_of_variables):
            satisfaction_of_one_doctor = []
            current_doctor = self.doctors.doctor_dataset.iloc[i]
            doctor_info = current_doctor.iloc[0:3].to_list()
            distant_list_from_curr_HT = list(self.areas.distances_dict[current_doctor.iloc[3]].values())

            area_info = self.areas.area_dataset.iloc[x[i], :].to_list()
            parameter_of_NN = [doctor_info[0], doctor_info[1], doctor_info[2], area_info[2], area_info[1], area_info[0], distant_list_from_curr_HT[x[i]]]
            satisfaction_in_area = self.NN_predictor.satisfaction_prediction(parameter_of_NN)
            satisfaction_of_all_doctors.append(satisfaction_in_area[0])
        #print(satisfaction_of_all_doctors)



        for i in range(len(satisfaction_of_all_doctors)):
            sum+= satisfaction_of_all_doctors[i]

        #using 35 - sum as max satisfaction is 5 and 8 doctors are used. So 8x5 = 35
        # should this be maximization or minimization? because as the overall satisfaction increases, result should decrease
        result = math.fabs(5*self.number_of_variables - sum)

        #dispersion function call
        dispersion_score = self.dispersion(x)
        #print(sum, " ", dispersion_score)
        solution.objectives[0] = -1*sum
        solution.objectives[1] = -1*dispersion_score

        return solution

    def get_name(self) -> str:
        return 'Doctor Allocation'

    def dispersion(self, solution_list):
        nd = 0
        sum_demand_supply = 0
        for i in range(len(self.demand_list)):
            allocation_in_city = list(filter(lambda x: x == i, solution_list))
            len_of_area = len(allocation_in_city)
            if len_of_area >= self.min_allocation_list[i]:
                nd += 1
            demand_met = len_of_area / self.demand_list[i]
            sum_demand_supply += demand_met

        #print("nd is ", nd, " and demand met is ", sum_demand_supply)
        return nd + sum_demand_supply


class Doctors():
    def __init__(self, filename):
        self.filename = filename
        self.doctor_dataset = None

    def write_doctor_dataset(self):
        doctor_to_write = pd.DataFrame(self.doctor_dataset)
        doctor_to_write.to_csv(
            r'/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/doctor_dataset.csv',
            index=False, header=True)
    def extract_doctor_info(self):
        self.doctor_dataset = pd.read_csv(self.filename)
        self.doctor_dataset = self.doctor_dataset[['0', '1', '2', '3']]
        #self.doctor_dataset = self.doctor_dataset.loc[self.doctor_dataset['2'] == "Medical Field (Doctor, Nurse, Nutritionist, Pharmacists and other Health Care workers etc)"]

    def turn_info_to_numeric(self):
        self.doctor_dataset["1"] = self.doctor_dataset["1"].replace(
            ["20-25", "26-30", "31-35", "36-40", "41 or Above"],
            [20, 26, 31, 36, 41])
        self.doctor_dataset["0"] = self.doctor_dataset["0"].replace(["Male", "Female", "Prefer not to disclose"], [1, 2, 3])
        self.doctor_dataset["2"] = self.doctor_dataset["2"].replace(
            ["Medical Field (Doctor, Nurse, Nutritionist, Pharmacists and other Health Care workers etc)",
             "Engineering and IT",
             "Business Field (Management, HR, Banking, Marketing etc)",
             "Academia (Teacher, Lecturer, Assistant/ Associate Professor, Professor)", "Student", "Unemployed",
             "Other"], [1, 2, 3, 4, 5, 6, 7])

        self.doctor_dataset = self.doctor_dataset.values

class Areas():
    def __init__(self, filename, distances_filename):
        self.area_dataset = pd.read_csv(filename)
        self.distanes_dataset = pd.read_csv(distances_filename)
        self.distanes_dataset = self.distanes_dataset[["From", "To", "Kilometers max"]]
        self.distances_dict = {}
    def categorize_schooling(self):
        self.area_dataset['School'] = np.where(self.area_dataset['School'] < 4.00, 1, self.area_dataset['School'])
        self.area_dataset['School'] = np.where(((self.area_dataset['School'] > 4.00) & (self.area_dataset['School'] < 6.00)) , 2, self.area_dataset['School'])
        self.area_dataset['School'] = np.where(self.area_dataset['School'] > 6.00, 3, self.area_dataset['School'] )

    def categorize_house_rent(self):
        self.area_dataset['Avg House Rent'] = np.where(self.area_dataset['Avg House Rent'] < 8000, 1, self.area_dataset['Avg House Rent'])
        self.area_dataset['Avg House Rent'] = np.where(
            ((self.area_dataset['Avg House Rent'] >= 8000) & (self.area_dataset['Avg House Rent'] < 10000)), 2,
            self.area_dataset['Avg House Rent'])
        self.area_dataset['Avg House Rent'] = np.where(self.area_dataset['Avg House Rent'] >= 10000, 3, self.area_dataset['Avg House Rent'])

    def categorize_security(self):
        self.area_dataset['Security'] = np.where(self.area_dataset['Security'] < 1000, 3, self.area_dataset['Security'])
        self.area_dataset['Security'] = np.where(
            ((self.area_dataset['Security'] >= 1000) & (self.area_dataset['Security'] < 2000)), 2,
            self.area_dataset['Security'])
        self.area_dataset['Security'] = np.where(self.area_dataset['Security'] >= 2000, 1,  self.area_dataset['Security'])

    def create_distance_dict(self):
        j = -1
        for i in range(self.distanes_dataset.shape[0]):
            if i % 7 == 0:
                j += 1
                self.distances_dict[self.distanes_dataset.at[i, 'From']] = {}
            distance_level = 0
            if self.distanes_dataset.at[i, 'Kilometers max'] <= 200:
                distance_level = 1
            elif self.distanes_dataset.at[i, 'Kilometers max'] > 200 and self.distanes_dataset.at[i, 'Kilometers max'] <= 400:
                distance_level = 2
            else:
                distance_level = 3
            self.distances_dict[self.distanes_dataset.at[i, 'From']][self.distanes_dataset.at[i, 'To']] = distance_level

class Optimize_Allocation():
    def __init__(self, num_of_trial, mutation_probability, crossover, mutation, number_of_city, demand_list, number_of_variables, max_evaluation):
        self.num_of_trial = num_of_trial
        self.mutation_probability = mutation_probability
        self.number_of_city = number_of_city
        self.demand_list = demand_list
        self.number_of_variables = number_of_variables
        self.max_evaluations = max_evaluation
        if crossover == 'single_point':
            self.crossover = IntegerSinglePointCrossover(probability=0.9)
        elif crossover == 'multi_point':
            self.crossover = IntegerMultiPointCrossover(probability=0.9)

        if mutation == 'domain':
            self.mutation = Domain_Knowledge_mutation(probability=mutation_probability, number_of_city=number_of_city, demand_list= demand_list )
        elif mutation == 'polynomial':
            self.mutation = IntegerPolynomialMutation(probability= mutation_probability, distribution_index=20)
        elif mutation == 'random':
            self.mutation = Random_Integer_Mutation(probability=mutation_probability, number_of_city=number_of_city)

    def allocate(self):
        problem = Find_Optimum_Allocation(number_of_variables=self.number_of_variables, demand_list=self.demand_list, number_of_city=self.number_of_city)
        #problem = Find_Optimum_Allocation(number_of_variables = 10, demand_list = [3, 3, 2, 2, 2, 2, 2],  number_of_city=7)
        '''
        algorithm = NSGAII(
        problem=problem,
        population_size=100,
        offspring_population_size=100,
        mutation=PolynomialMutation(probability=1.0 / problem.number_of_variables, distribution_index=20),
        crossover=SBXCrossover(probability=1.0, distribution_index=20),
        termination_criterion=StoppingByEvaluations(max_evaluations=100),
        dominance_comparator=DominanceComparator()
        )
        '''
        algorithm = NSGAII(
            problem=problem,
            population_size=100,
            offspring_population_size=100,
            mutation=self.mutation,
            crossover=self.crossover,
            termination_criterion=StoppingByEvaluations(max_evaluations=self.max_evaluations),
            dominance_comparator=DominanceComparator()
        )

        algorithm.run()
        #result = get_non_dominated_solutions(algorithm.get_result())
        result = algorithm.get_result()

        print_function_values_to_file(result, '/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/Results/FUN/FUN.' + algorithm.label+' Trial '+str(self.num_of_trial))
        print_variables_to_file(result, '/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/Results/VAR/VAR.' + algorithm.label+' Trial '+ str(self.num_of_trial))
        print('Algorithm: {}'.format(algorithm.get_name()))
        print('Problem: {}'.format(problem.get_name()))
        #print('Solution: {}'.format(result.variables))
        #print('Fitness: {}'.format(result.objectives[0]))
        print('Computing time: {}'.format(algorithm.total_computing_time))

        plot_front = Plot(title='Pareto front approximation', axis_labels=['X', 'Y'])
        png_name = "/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/Results/Plots/NSGAII-Doctor_Trial"+str(self.num_of_trial)
        plot_front.plot(result, label='NSGAII-Allocation', filename=png_name, format='png')


'''


#print(areas.distances_dict)
#print(areas.distanes_dataset)

if __name__ == '__main__':
    problem = DTLZ2()
    problem.reference_front = read_solutions(filename='resources/reference_front/DTLZ2.3D.pf')

    max_evaluations = 25000
    algorithm = NSGAII(
        problem=problem,
        population_size=100,
        offspring_population_size=100,
        mutation=PolynomialMutation(probability=1.0 / problem.number_of_variables, distribution_index=20),
        crossover=SBXCrossover(probability=1.0, distribution_index=20),
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations),
        dominance_comparator=DominanceComparator()
    )

     
    algorithm.run()
    front = algorithm.get_result()

    # Save results to file
    print_function_values_to_file(front, 'FUN.' + algorithm.label)
    print_variables_to_file(front, 'VAR.'+ algorithm.label)

    print(f'Algorithm: ${algorithm.get_name()}')
    print(f'Problem: ${problem.get_name()}')
    print(f'Computing time: ${algorithm.total_computing_time}')
'''


'''
#Trial 1
optimize_allocation = Optimize_Allocation(num_of_trial=1, mutation_probability=0.2)
optimize_allocation.allocate()

#Trial 2
optimize_allocation = Optimize_Allocation(num_of_trial=2, mutation_probability=0.25)
optimize_allocation.allocate()


#Trial 3
optimize_allocation = Optimize_Allocation(num_of_trial=3, mutation_probability=0.3, crossover="single_point")
optimize_allocation.allocate()


#Trial 4
optimize_allocation = Optimize_Allocation(num_of_trial=4, mutation_probability=0.4, crossover="multi_point")
optimize_allocation.allocate()


#Trial 5
optimize_allocation = Optimize_Allocation(num_of_trial=5, mutation_probability=0.2, crossover="multi_point")
optimize_allocation.allocate()


#Trial 6
optimize_allocation = Optimize_Allocation(num_of_trial=6, mutation_probability=0.2, crossover="multi_point", number_of_variables = 10, demand_list = [3, 3, 2, 2, 2, 2, 2],  number_of_city=7, mutation='custom')
optimize_allocation.allocate()

#Trial 7
optimize_allocation = Optimize_Allocation(num_of_trial=7, mutation_probability=0.25, crossover="multi_point", number_of_variables = 20, demand_list = [3, 5, 4, 5, 2, 2, 5],  number_of_city=7, mutation='custom', max_evaluation = 300000)
optimize_allocation.allocate()

#Trial 8
optimize_allocation = Optimize_Allocation(num_of_trial=8, mutation_probability=0.3, crossover="multi_point", number_of_variables = 20, demand_list = [3, 5, 4, 5, 2, 2, 5],  number_of_city=7, mutation='custom', max_evaluation = 200000)
optimize_allocation.allocate()


#Trial 9
optimize_allocation = Optimize_Allocation(num_of_trial=9, mutation_probability=0.4, crossover="multi_point", number_of_variables = 20, demand_list = [3, 5, 4, 5, 2, 2, 5],  number_of_city=7, mutation='custom', max_evaluation = 200000)
optimize_allocation.allocate()

for i in range(50):
    optimize_allocation = Optimize_Allocation(num_of_trial=(i+10), mutation_probability=0.3, crossover="single_point",
                                              number_of_variables=20, demand_list=[3, 5, 4, 5, 2, 2, 4],
                                              number_of_city=7, mutation='random', max_evaluation=300000)
    optimize_allocation.allocate()
    
'''
for i in range(50):
    optimize_allocation = Optimize_Allocation(num_of_trial=(i+60), mutation_probability=0.3, crossover="multi_point",
                                              number_of_variables=20, demand_list=[3, 5, 4, 5, 2, 2, 4],
                                              number_of_city=7, mutation='random', max_evaluation=300000)
    optimize_allocation.allocate()