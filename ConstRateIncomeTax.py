
import random
import math
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

import IncomeTax as income


# 所得税（税率一定）
class ConstRateIncomeTax(income.IncomeTax):

    _MinIncomeForTaxation = 0.175903
    _TaxRate = 0.05

    def __init__(self, redistribution=False):
        super().__init__(graphTitle="一定税率の所得税", redistribution=redistribution, limit=500000)
        self._TaxationPerTime = 10

    # def subProcess(self, agents):
    #     for agent in agents:
    #         if self._MinIncomeForTaxation > agent.wealth:
    #             continue

    #         agent.wealth *= (1 - self.taxRate)

    def getTaxRate(self, agent):
        if self._MinIncomeForTaxation > agent.wealth:
            return 0
        else:
            return self._TaxRate