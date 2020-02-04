

class A:
    def __init__(self):
        print("A: __init__")

    def Method(self):
        print("A: Method")
    

class B:
    def __init__(self):
        print("B: __init__")

    def Method(self):
        print("B: Method")
    

class Sub(A, B):
    def __init__(self):
        print("sub")
    
    def Method(self):
        super().Method()            # Aの関数が呼ばれる
        super(A, self).Method()     # Bの関数が呼ばれる
        super(B, self).Method()