


class Fib:

    def getFibonacci(self, n):
        # 5 - 1 1 2 3 5
        a = 0
        b = 1
        c = 0
        i = 0
        while i < n:
            print(a)
            a, c = b, a+b
            b = c
            i+=1

    def fib(self, n):
        if n <=1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)

obj = Fib()
print(obj.getFibonacci(5))

# t = (1,'a',[1,2,3,4])
#
# t[2].append(5)
# print(t)
#
# ip  = "This is Abhinav I live in India"
# op  = [["This" ,"is"],["is","Abhinav"],["Abhinav","I"], ["x", 'y']]
# #op[:3]
# ip1 = ip.split(' ')
#
# print([ip1[i:i+3] for i in range(len(ip1)-2)])
#
#
# #
# # ip1 = ip.split(' ')
# # ip2 = ip1[1:]
# # print([list(i) for i in zip(ip1,ip2)])
#
#
#
#
# # obj = Fib()
# # print(obj.getFibonacci(5))
#
# class CoffeeVendingMachine:
#
#     # ingredients
#     # dispense
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     def __process(self, ig):
#         pass
#
#     def process(self, ig):
#         return self.__process(ig)
#
#     def dispense(self):
#         try:
#             if self.process(self.ingredients):
#
#                 print(f"Here are my ingredients....{self.ingredients.items()}")
#             else:
#                 print("Wait still processing....")
#         except Exception:
#             pass
#
# c = CoffeeVendingMachine({'milk':20, 'coffee_powder':1})

