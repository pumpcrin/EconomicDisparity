

class SuperClass:
    def __init__(self, parameter):
        self.field = parameter

    def standard(self, param):
        print(f"standard: {self}")
    
    def subProcess(self):
        print("subProcess-Super")

    def virtual(self, param):
        print("virtual")
        self.subProcess()
    

    # これはエラーの原因になる（関数の1つ目の引数にはそのクラス自身の参照が入る）
    # def nonSelf(param):
    #     print("nonSelf")