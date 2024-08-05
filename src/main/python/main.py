# Main python file

print('Hello, world of Python!')

# Data types
str1 = 'String'
boolean = True
float1 = 25.5
int1 = 7
list1 = [2,4,6,8]
set1 = {2,4,6,8}
dict1 = {'name':'Mark','age':37}
tup1 = (2,4,6)
list2 = [str1,boolean,float1,int1,list1,set1,dict1,tup1]
for i in list2:
    print(f'Data type: {type(i)}')

# Arithmetic
my_int = 7
power = 3
print(f'My number {my_int} to the power of {power}: {my_int ** power}')
if type(my_int) == int:
    print('This is an integer')
else:
    print('Not an integer')

# Strings
my_str = 'May the force be with you!'
print(my_str[-1:-8:-1])
print(my_str[-12:-1:1])
print(my_str[-1::-1])
print(my_str[::-1])
my_str2 = my_str.upper()
my_str3 = my_str.split()
for i in my_str3:
    print(i)
print(my_str2)
str2 = 'Mark,Newcomb,37,Male,Employed=True'
str3 = str2.split(',')
print(str3)
str4 = str3[4].split('=')
str5 = str4[1]
print(str3)
print(str5)
str3.pop()
print(f'{str3} : {str5}')
str3.append(str5)
print(str3)