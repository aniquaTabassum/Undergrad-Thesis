import os
import unittest

from jmetal.core.quality_indicator import HyperVolume
import numpy as np
from JMetal import Results
from JMetal import global_config


class HypervolumeCalculation():
    def __init__(self):
        None

    def calculateHV(self, tp_path_name, fun_path_name):
        directory = global_config._base_dir + "JMetal/Results/Merged Results/Setting 1"

        # front contains the entries of true pareto front
        front = []
        with open(tp_path_name) as file:
            for line in file:
                vector = [float(x) for x in line.split()]
                front.append(vector)


        for filename in os.listdir(directory):
            file = os.path.join(directory, filename)
            with open(file) as file:
                for line in file:
                    # reference point consists of a pair of value from FUN file
                    reference_point = [float(x) for x in line.split()]
                    hv = HyperVolume(reference_point)
                    value = hv.compute(np.array(front))
                    print(value)


if __name__ == "__main__":
    hv = HypervolumeCalculation()
    tp_name = global_config.tp_path
    fun_name = "/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/Results/Merged Results/Setting 2/FUN.NSGAII.Doctor Allocation Trial 64"
    hv.calculateHV(tp_path_name=tp_name, fun_path_name=fun_name)
