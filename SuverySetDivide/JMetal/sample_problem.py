from jmetal.algorithm.multiobjective import NSGAII
from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.core.problem import FloatProblem, IntegerProblem
from jmetal.core.solution import FloatSolution, IntegerSolution
from jmetal.operator import BinaryTournamentSelection, PolynomialMutation, SBXCrossover, IntegerPolynomialMutation
from jmetal.operator.crossover import IntegerSBXCrossover
from jmetal.problem.singleobjective.unconstrained import Rastrigin
from jmetal.util.comparator import DominanceComparator
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations
import math
from FinalWeights import LinearRegression
from Allocate_Doctors import Doctors
class Find_Optimum_Allocation(IntegerProblem):

    def __init__(self, number_of_variables: int = 2):
        super(Find_Optimum_Allocation, self).__init__()
        self.doctors = Doctors("doctor_dataset.csv")
        self.doctors.extract_doctor_info()
        self.doctors.doctor_dataset = self.doctors.doctor_dataset[0:8]

        self.NN_predictor = LinearRegression.FindWeight()
        self.NN_predictor.weightCalculate()
        self.number_of_objectives = 1
        self.number_of_variables = number_of_variables
        self.number_of_constraints = 0

        self.obj_directions = [self.MAXIMIZE]
        self.obj_labels = ['satisfaction(x)']

        self.lower_bound = [0 for _ in range(number_of_variables)]
        self.upper_bound = [7 for _ in range(number_of_variables)]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    def evaluate(self, solution: IntegerSolution) -> IntegerSolution:

        x = solution.variables
        print(x)
        sum = 0
        for i in range(len(x)):
            sum+= x[i]
        #using 35 - sum as max satisfaction is 5 and 7 doctors are used. So 7x5 = 35
        result = math.fabs( 35 - sum)

        solution.objectives[0] = result

        return solution

    def get_name(self) -> str:
        return 'sum of 2 numbers'

if __name__ == '__main__':
    problem = Find_Optimum_Allocation(10)

    algorithm = NSGAII(
        problem=problem,
        population_size=100,
        offspring_population_size=100,
        mutation=PolynomialMutation(probability=1.0 / problem.number_of_variables, distribution_index=20),
        crossover=SBXCrossover(probability=1.0, distribution_index=20),
        termination_criterion=StoppingByEvaluations(max_evaluations=100),
        dominance_comparator=DominanceComparator()
    )


    algorithm.run()
    result = algorithm.get_result()

    print_function_values_to_file(result, 'FUN.' + algorithm.label)
    print_variables_to_file(result, 'VAR.' + algorithm.label)
    print('Algorithm: {}'.format(algorithm.get_name()))
    print('Problem: {}'.format(problem.get_name()))
    #print('Solution: {}'.format(result.variables))
    print('Fitness: {}'.format(result.objectives[0]))
    print('Computing time: {}'.format(algorithm.total_computing_time))