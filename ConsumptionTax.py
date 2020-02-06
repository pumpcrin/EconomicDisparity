
import random
import math
import matplotlib.pyplot as plt
from matplotlib import rcParams

import CalculatePattern as cp

# 消費税（所得譲渡時に、10%を回収 => gainRate=0.9）
class ConsumptionTax(cp.CalculatePattern):

  def __init__(self):
      super().__init__("消費税あり", gainRate = 0.9)

  def process(self, time, agents):
    for i in range(time):
      self.giveMoney(agents)

      self.redistribute(i, agents)
      