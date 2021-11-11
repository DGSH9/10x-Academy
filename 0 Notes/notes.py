var = 'abc'    #string is immutable
print(id(var))
var = var + 'f'
print(id(var),)

arr1 = ['abc'] #lsit is mutable
print(id(arr1))
arr1.append('fgh')
print(id(arr1))