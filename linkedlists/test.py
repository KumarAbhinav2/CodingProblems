def process():
    try:
        print("Hello")
        raise ValueError
    except ValueError:
        print("Having exception")
        raisels



process()
print("Still continuing....")

from collections import OrderedDict

a = OrderedDict()

a.move_to_end()