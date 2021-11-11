# def sample_problem(arg_1,arg_2,*args):
#     print('Arg_1',arg_1)
#     print('Arg_2',arg_2)
#     print('args',args)
#     for val in args:
#         print(val)
# sample_problem(1,2,3,4,5,6,7,8,9)


# # Dictionary Notation
# def sample_problem2(arg_1,**kwargs):
#     print(kwargs)
#     # print(kwargs['Durgesh1'])
#     print(arg_1)

# sample_problem2(25,Durgesh = '21',Ron=23)


# Input
# Price

# Output
# sale value

# def calculate_sale_value(quantity,price):
#     return quantity*price
# quantity = 7
# price = 20
# print(calculate_sale_value(quantity,price))


def calculate_sale_value(quantity, price=20):
    return quantity*price


quantity = 7
price = 25
print(calculate_sale_value(quantity, price=25))


# Default Value
def calculate_sale_value(quantity, price=20):
    return quantity*price


quantity = 7
print(calculate_sale_value(quantity))

###################


def calculate_sale_value(quantity, price=20, biscuit_type="chocolate"):
    print('quantity', quantity)
    print('price', price)
    print('biscuit_type', biscuit_type)
    return quantity*price


quantity = 7
print(calculate_sale_value(quantity))
