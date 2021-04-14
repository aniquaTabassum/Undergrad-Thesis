# import random
#
# from jmetal.algorithm.multiobjective.gde3 import GDE3
# from jmetal.algorithm.multiobjective.nsgaii import NSGAII
# from jmetal.algorithm.multiobjective.smpso import SMPSO
# from jmetal.core.problem import BinaryProblem, FloatProblem
# from jmetal.core.quality_indicator import *
# from jmetal.core.solution import BinarySolution, FloatSolution
# from jmetal.lab.experiment import Experiment, Job, generate_summary_from_experiment
# from jmetal.operator import PolynomialMutation, SBXCrossover, SPXCrossover, BitFlipMutation
# from jmetal.problem import ZDT1, ZDT2, ZDT3
# from jmetal.util.archive import CrowdingDistanceArchive
# from jmetal.util.termination_criterion import StoppingByEvaluations
# from jmetal.algorithm.multiobjective.nsgaii import NSGAII
# from jmetal.operator import SBXCrossover, PolynomialMutation
# from jmetal.problem import ZDT1
# from jmetal.util.termination_criterion import StoppingByEvaluations
# from jmetal.lab.visualization.plotting import Plot
# from jmetal.util.solution import get_non_dominated_solutions
#
#
#
#
# class SubsetSum(BinaryProblem):
#
#    def __init__(self, C: int, W: list):
#       super(SubsetSum, self).__init__()
#       self.C = C
#       self.W = W
#
#       self.number_of_bits = len(self.W)
#       self.number_of_objectives = 1
#       self.number_of_variables = 1
#       self.number_of_constraints = 0
#
#       self.obj_directions = [self.MAXIMIZE]
#       self.obj_labels = ['Sum']
#
#    def evaluate(self, solution: BinarySolution) -> BinarySolution:
#       pass
#
#    def create_solution(self) -> BinarySolution:
#       pass
#
#    def get_name(self) -> str:
#       return 'Subset Sum'
#
#    def evaluate(self, solution: BinarySolution) -> BinarySolution:
#        total_sum = 0.0
#
#        for index, bits in enumerate(solution.variables[0]):
#            if bits:
#                total_sum += self.W[index]
#
#        if total_sum > self.C:
#            total_sum = self.C - total_sum * 0.1
#
#            if total_sum < 0.0:
#                total_sum = 0.0
#
#        solution.objectives[0] = -1.0 * total_sum
#
#        return solution
#
#    def create_solution(self) -> BinarySolution:
#        new_solution = BinarySolution(number_of_variables=self.number_of_variables,
#                                      number_of_objectives=self.number_of_objectives)
#        new_solution.variables[0] = \
#            [True if random.randint(0, 1) == 0 else False for _ in range(self.number_of_bits)]
#
#        return new_solution
#
# problem = SubsetSum(12.0, [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 9.0])
#
# max_evaluations = 25000
# algorithm = NSGAII(
#     problem=problem,
#     population_size=100,
#     offspring_population_size=100,
#     mutation=BitFlipMutation(probability=1.0 / problem.number_of_variables),
#     crossover=SPXCrossover(probability=1.0),
#     termination_criterion=StoppingByEvaluations(max_evaluations)
# )
#
# algorithm.run()
# solutions = algorithm.get_result()
# front = get_non_dominated_solutions(solutions)
# print(front[0])
#
# plot_front = Plot(title='Pareto front approximation')
# plot_front.plot(front, label='NSGAII-SubsetSum')