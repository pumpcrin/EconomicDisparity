
import random
import math
import os.path
import shutil
import datetime
import matplotlib.pyplot as plt
import matplotlib as mt
import matplotlib.animation as animation
import numpy as np
from matplotlib import rcParams

from PIL import Image
import glob


rcParams['font.family'] = 'Meiryo'

import Tools as tl
import CalculatePattern as cp
import ConsumptionTax as consump
import IncomeTax as income
import StageIncomeTax as stageIncome
import ConstRateIncomeTax as constRateIncome


class Agent:
  def __init__(self, unique_id, initial_wealth):
    self.unique_id = unique_id    # id番号
    self.wealth = initial_wealth  # 初期資産
  

#政策の選択
patterns = []

patterns.append(cp.CalculatePattern("政策なし"))
patterns.append(consump.ConsumptionTax())
patterns.append(income.IncomeTax())
patterns.append(stageIncome.StageIncomeTax())
patterns.append(constRateIncome.ConstRateIncomeTax())

print("政策リスト")
for i, pattern in enumerate(patterns):
  print(f"{i}:{pattern.graphTitle}")
patternNum = tl.SafetyIntegerInput("施行する政策を選択してください：")

pattern = patterns[patternNum]

redistribution = False
if patternNum != 0:
  redistribution = tl.SafetyIntegerInput("徴収した税を全体に再分配しますか？（1:はい, 0:いいえ）")

pattern.initialize(redistribution)


#フォルダ名
now = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
dir = f"{pattern.path}/{now}"
os.makedirs(dir, exist_ok=True)

#条件をテキストファイルに出力
status = [(pattern.graphTitle, "政策"), \
          (pattern.n, "人口"), \
          (pattern.limit, "最大譲渡回数"), \
          (pattern.firstSave, "初期所得"), \
          (pattern.givingMoney, "1回の譲渡で失う所得"), \
          (pattern.gainMoney, "1回の譲渡で得る所得")]

status = pattern.additionalWriteParams(status)
statusText = [f"{tuple[1]}\t= {tuple[0]}" for tuple in status]
with open(dir+"/status.txt", mode="w") as f:
  f.writelines("\n".join(statusText))

ginis = []
ims = []

# fig = plt.figure()

# 各譲渡回数でグラフ描画
for i, time in enumerate(pattern.times):

  print(f"【{i+1}つ目のグラフ】")

  agents = [Agent(i, pattern.firstSave) for i in range(pattern.n)]
  count = 0

  fig = plt.figure()
  
  pattern.process(time, agents)

  agent_wealth = [a.wealth for a in agents]
  G = pattern.gini(agent_wealth)
  ginis.append(G)

  print("G = "+str(G) + ", time = "+str(time))

  bins = np.ceil((max(agent_wealth) - min(agent_wealth)) / pattern.gainMoney)

  # lines, *_ = plt.hist(agent_wealth, bins = int(bins))
  plt.hist(agent_wealth, bins = int(bins))
  plt.title(f'{pattern.graphTitle} (t = {time}, G = {G})')

  # ims.append([lines])
  plt.savefig(dir+f"/譲渡回数{time}.png")


# ani = animation.ArtistAnimation(fig, ims)
# ani.save("anim.gif", writer="imagemagick")
plt.show()


plt.clf()
fig = plt.figure()
plt.plot(pattern.times, ginis, lineStyle="dashed", marker="o")
plt.title("ジニ係数の推移")
plt.savefig(dir+f"/ジニ係数推移.png")
plt.show()

notSaveFlag = tl.SafetyIntegerInput('結果を出力しますか？(はい: 0, いいえ: 1以上)', 0)
if(notSaveFlag):
  shutil.rmtree(dir)

# gifFlag = tl.tl.SafetyIntegerInput('結果をgif化しますか？(はい: 0, いいえ: 1以上)', 0)
# if(not gifFlag):
  # tl.saveGif("./"+pattern.graphTitle, dir, f"{now}.gif")