import random

# 政策ごとに変わりそうなところだけクラス化、このまま使うと政策なしになる
class CalculatePattern:

    _RedistributionPerTime = 10

    def __init__(self, graphTitle, redistribution=False, firstSave=100, limit=5000000, n=1000, givingMoney=5, gainRate=1):
        if redistribution:
            graphTitle += ", 再分配あり"
        else:
            graphTitle += ", 再分配なし"
        
        self.graphTitle = graphTitle
        self.redistribution = redistribution
        self.firstSave = firstSave

        self.firstSave = firstSave
        self.limit = limit
        self.n = n
        self.givingMoney = givingMoney
        self.gainMoney = givingMoney * gainRate
        self.treasury = 0

    def initialize(self):
        limit = self.limit

        timeBases = [1, 2, 5]
        times = []
        order = 1
        while(order <= limit):
            order *= 10
            times += [i*order for i in timeBases]

        self.times = [time for time in times if time <= limit]
        if not limit in times:
            times.append(limit)
        print(f"times: {times}")

                        
    def giveMoney(self, agents):
        agent1 = random.choice(agents)
        agent2 = random.choice(agents)

        if agent1.wealth >= self.givingMoney:
            agent2.wealth += self.gainMoney
            agent1.wealth -= self.givingMoney
            taxation(givingMoney - gainMoney)

    def gini(self, y):
        y.sort()
        n = len(y)
        nume = 0

        for i in range(n):
            nume = nume + (i + 1)* y[i]
            deno = n * sum(y)

        return ((2*nume)/deno - (n+1)/(n))*(n/(n-1))

    def process(self, time, agents):
        for i in range(time):
            self.giveMoney(agents)

            if i % _RedistributionPerTime == 0 and self.redistribution:
                self.redistribute(agents)

    def redistribute(self, agents):
        subsidy = treasury / len(agents)
        for agent in agents:
            agent.wealth += subsidy

        treasury = 0

    def taxation(self, money):
        treasury += money