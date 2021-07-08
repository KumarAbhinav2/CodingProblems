"""
Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the
left and positive elements appear at the right of the list.

we will treat zero as a positive integer for this challenge.

Input = [10,-1,20,4,5,-9,-6]
Output = [-1,-9,-6,10,20,4,5]

"""

# Intuitive

def rearrange_intuitive(lst):
    neg_lst = []
    pos_lst = []
    for i in lst:
        if i < 0:
            neg_lst.append(i)
        elif i >=0:
            pos_lst.append(i)
    return neg_lst+pos_lst