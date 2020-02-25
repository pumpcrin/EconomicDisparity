
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
    _MaxRateMinMoney_InSimu = 700

    def __init__(self, graphTitle="所得税あり（連続的）", limit=500000):
        super().__init__(graphTitle, limit=limit)
        self._TaxationPerTime = super()._RedistributionPerTime


    
    def initialize(self, redistribution=False):
        super().initialize(redistribution=redistribution)
        self.m = self._MaxRateMinMoney_InReal / self._MaxRateMinMoney_InSimu
        

    def process(self, currentTime, time, agents):
        print(f"taxation: {self._TaxationPerTime}")
        while currentTime <= time:
        # for i in range(time):
            super().giveMoney(agents)
            if currentTime != 0 and currentTime % self._TaxationPerTime == 0:
                self.subProcess(agents)

            self.redistribute(currentTime, agents)
            currentTime += 1

    def subProcess(self, agents):
        for agent in agents:
            if agent.wealth == 0:
            # if agent.wealth < self._MinIncomeForTaxation:
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

    def additionalWriteParams(self, status):
        status = super().additionalWriteParams(status)
        status += [(self._TaxationPerTime, "課税の間隔"), (f"{self._MaxRateMinMoney_InReal}/{self._MaxRateMinMoney_InSimu}={self.m}", "横軸の縮小倍率")]
        return status