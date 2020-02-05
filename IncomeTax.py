
import random
import math
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

import CalculatePattern as cp


#所得税（連続的：税率と所得が1対1で対応）
class IncomeTax(cp.CalculatePattern):

    _Coef_RateFormula = 12.041
    _Bias_RateFormula = 58.859
    _MaxRateMinMoney_InReal = 4000
    _MaxRateMinMoney_InSimu = 350

    def __init__(self, graphTitle="所得税あり（連続的）", redistribution=False, limit=50000):
        super().__init__(graphTitle, redistribution=redistribution, limit=limit)
        self._TaxationPerTime = super()._RedistributionPerTime


    
    def initialize(self):
        super().initialize()
        self.m = self._MaxRateMinMoney_InReal / self._MaxRateMinMoney_InSimu
        

    def process(self, time, agents):

        for i in range(time):
            super().giveMoney(agents)
            if i != 0 and i % self._TaxationPerTime == 0:
                self.subProcess(agents)
    

    def subProcess(self, agents):
        for agent in agents:
            if agent.wealth == 0:
                continue

            # percentage = self._Coef_RateFormula*np.log(agent.wealth*self.m) - self._Bias_RateFormula

            # if percentage < 0:
            #     percentage = 0
            taxRate = self.getTaxRate(agent)

            tax = agent.wealth * taxRate
            agent.wealth -= tax
            self.taxation(tax)

    # 小数点で表した税率を返す
    def getTaxRate(self, agent):
        taxPercentage = self._Coef_RateFormula*np.log(agent.wealth*self.m) - self._Bias_RateFormula
        taxRate = taxPercentage / 100

        if taxRate < 0:
            taxRate = 0

        return taxRate

