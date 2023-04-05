class base:
    def __init__(self):
        self.id = 234

class sub(base):
    def __init__(self):
        #self.id = 0
        super().__init__()

A = sub()
print(A.id)