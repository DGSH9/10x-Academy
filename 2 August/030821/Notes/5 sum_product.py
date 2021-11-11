

def sum_product(num1,num2):
    sum_num=num1+num2
    product_num=num1*num2
    return {'sum':sum_num,'product':product_num}

val_1=int(input())
val_2=int(input())

result =sum_product(val_1,val_2)

print('Sum',result['sum'])
print('Product',result['product'])