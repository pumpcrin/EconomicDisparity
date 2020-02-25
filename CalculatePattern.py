import random

# 政策ごとに変わりそうなところだけクラス化、このまま使うと政策なしになる
class CalculatePattern:

    _RedistributionPerTime = 1000

    def __init__(self, graphTitle, firstSave=100, limit=500000, n=1000, givingMoney=5, gainRate=1):
        # if redistribution:
        #     graphTitle += ", 再分配あり"
        # else:
        #     graphTitle += ", 再分配なし"
        
        
        self.graphTitle = graphTitle
        self.firstSave = firstSave

        self.firstSave = firstSave
        self.limit = limit
        self.n = n
        self.givingMoney = givingMoney
        self.gainMoney = givingMoney * gainRate
        self.treasury = 0

    def initialize(self, redistribution=False):
        redisStr = "再分配" + ("あり" if redistribution else "なし")
        self.path = self.graphTitle + "/" + redisStr
        self.graphTitle += ", " + redisStr
        self.redistribution = redistribution
        
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
            self.taxation(self.givingMoney - self.gainMoney)

    def gini(self, y):
        y.sort()
        n = len(y)
        nume = 0

        for i in range(n):
            nume = nume + (i + 1)* y[i]
            deno = n * sum(y)

        return ((2*nume)/deno - (n+1)/(n))*(n/(n-1))

    def process(self, currentTime, time, agents):
        while currentTime <= time:
        # for i in range(time):
            self.giveMoney(agents)
            currentTime += 1

            # if i % self._RedistributionPerTime == 0 and self.redistribution:
            #     self.redistribute(agents)

    def redistribute(self, i, agents):
        if i % self._RedistributionPerTime != 0 or (not self.redistribution):
            return

        subsidy = self.treasury / len(agents)
        for agent in agents:
            agent.wealth += subsidy

        self.treasury = 0

    def taxation(self, money):
        self.treasury += money

    def additionalWriteParams(self, status):
        status += [(self._RedistributionPerTime, "再分配の間隔")]
        return status