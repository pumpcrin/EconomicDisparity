import test2

class SubClass(test2.SuperClass):
    def __init__(self):
        super().__init__("aiu")
    
    def subProcess(self):
        print("subProcess-Sub")

    def virtual(self, param):
        super().virtual(param)
        print("sub-virtual")
    

    def callStandard(self):
        print(f"self: {self}")
        super().standard("aiuo")