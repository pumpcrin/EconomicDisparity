
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

    def __init__(self):
        super().__init__(graphTitle="一定税率の所得税", limit=500000)

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

    def additionalWriteParams(self, status):
        status = super().additionalWriteParams(status)
        status += [(self._TaxRate, "税率"), (self._MinIncomeForTaxation, "課税し始める所得")]

        return status