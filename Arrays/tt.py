class A:
    def __str__(self):
        return '1'

class B(A):
    def __init__(self):
        super().__init__()

class C(B):
    def __init__(self):
        super().__init__()

def main():
    o1 = B()
    o2 = A()
    o3 = C()
    print(o1, o2, o3)

main()