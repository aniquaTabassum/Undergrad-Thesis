import copy
import random
from typing import List

from jmetal.core.operator import Crossover
from jmetal.core.solution import Solution, FloatSolution, BinarySolution, PermutationSolution, IntegerSolution, \
    CompositeSolution
from jmetal.util.ckecking import Check

class IntegerSinglePointCrossover((Crossover[IntegerSolution, IntegerSolution])):
    def __init__(self, probability: float):
        super(IntegerSinglePointCrossover, self).__init__(probability=probability)


    def execute(self, parents: List[IntegerSolution]) -> List[IntegerSolution]:
        Check.that(issubclass(type(parents[0]), IntegerSolution), "Solution type invalid")
        Check.that(issubclass(type(parents[1]), IntegerSolution), "Solution type invalid")
        Check.that(len(parents) == 2, 'The number of parents is not two: {}'.format(len(parents)))
        random_crossover_point = random.randint(0, len(parents[0].variables) - 1)
        offspring = [copy.deepcopy(parents[0]), copy.deepcopy(parents[1])]
        random_probability = random.random()
        if random_probability <= self.probability:
            for i in range(random_crossover_point+1, len(parents[0].variables)):
                temp = offspring[0].variables[i]
                offspring[0].variables[i] = offspring[1].variables[i]
                offspring[1].variables[i] = temp

        return offspring

    def get_number_of_parents(self) -> int:
        return 2

    def get_number_of_children(self) -> int:
        return 2

    def get_name(self) -> str:
        return 'Single Point Crossover'


class IntegerMultiPointCrossover((Crossover[IntegerSolution, IntegerSolution])):
    def __init__(self, probability: float):
        super(IntegerMultiPointCrossover, self).__init__(probability=probability)

    def execute(self, parents: List[IntegerSolution]) -> List[IntegerSolution]:
        Check.that(issubclass(type(parents[0]), IntegerSolution), "Solution type invalid")
        Check.that(issubclass(type(parents[1]), IntegerSolution), "Solution type invalid")
        Check.that(len(parents) == 2, 'The number of parents is not two: {}'.format(len(parents)))
        random_crossover_point1 = random.randint(0, len(parents[0].variables) - 1)
        random_crossover_point2 = random.randint(0, len(parents[0].variables) - 1)
        offspring = [copy.deepcopy(parents[0]), copy.deepcopy(parents[1])]
        random_probability = random.random()
        if random_probability <= self.probability:
            for i in range(min(random_crossover_point1, random_crossover_point2)+1, max(random_crossover_point1, random_crossover_point2)-1):
                temp = offspring[0].variables[i]
                offspring[0].variables[i] = offspring[1].variables[i]
                offspring[1].variables[i] = temp

        return offspring

    def get_number_of_parents(self) -> int:
        return 2

    def get_number_of_children(self) -> int:
        return 2

    def get_name(self) -> str:
        return 'Multi Point Crossover'
