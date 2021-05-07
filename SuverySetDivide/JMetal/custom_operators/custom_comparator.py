import math
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from jmetal.core.solution import Solution
from jmetal.util.comparator import OverallConstraintViolationComparator
from jmetal.util.constraint_handling import overall_constraint_violation_degree

S = TypeVar('S')


class Comparator(Generic[S], ABC):

    @abstractmethod
    def compare(self, solution1: S, solution2: S) -> int:
        pass


class ObjectiveAndConstraintComparator(Comparator):

    def __init__(self, constraint_comparator: Comparator = OverallConstraintViolationComparator()):
        self.constraint_comparator = constraint_comparator

    def compare(self, solution1: Solution, solution2: Solution) -> int:
        if solution1 is None:
            raise Exception("The solution1 is None")
        elif solution2 is None:
            raise Exception("The solution2 is None")

        result = self.constraint_comparator.compare(solution1, solution2)
        if result == 0:
            value1 = solution1.objectives[0]
            value2 = solution2.objectives[0]

            if value1 < value2:
                result = -1
            elif value1 > value2:
                result = 1
            else:
                result = 0;

        return result