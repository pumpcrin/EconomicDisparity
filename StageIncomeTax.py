
import random
import math
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

import IncomeTax as income


# 所得税（段階的：所得が～以上で税率が～％）
class StageIncomeTax(income.IncomeTax):

    # taxPairs = [(17.5903, 5), (26.6448, 10), (61.1354, 20), (78.4326, 23), (179.9601, 33), (321.8488, 40)]
    taxationPerTime = 10

    def __init__(self, redistribution=False):
        super().__init__(graphTitle="段階的所得税", redistribution=redistribution, limit=5000000)

    def initialize(self):
        super().initialize()
        taxRates = [5, 10, 20, 23, 33, 40]
        # self.taxPairs = [(np.exp((taxRate + self._Bias_RateFormula)/self._Coef_RateFormula) / self.m, taxRate) for taxRate in taxRates]
        self.taxPairs = [(np.exp((taxRate + self._Bias_RateFormula)/self._Coef_RateFormula), taxRate) for taxRate in taxRates]
        print("initialize: StageIncomeTax")
        print(self.taxPairs)

    # def subProcess(self, agents):
    #     for agent in agents:
    #         # if agent.wealth == 0:
    #         #     continue
            
    #         taxRate = 0
    #         for taxPair in self.taxPairs:
    #             if agent.wealth < taxPair[0]:
    #                 break
    #             taxRate = taxPair[1]

    #         tax = taxRate/100
    #         # agent.wealth *= (1 - tax/100)
    #         agent.wealth -= tax
    #         taxation(tax)

    def getTaxRate(self, agent):

        taxRate = 0
        for taxPair in self.taxPairs:
            if agent.wealth < taxPair[0]:
                break
            taxRate = taxPair[1]
        
        return taxRate
