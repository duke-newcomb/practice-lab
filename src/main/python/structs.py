# Data structures

in_stock_status = {'Mustang':True,'F-150':True,'Taurus':False,'Focus':False,'Mach-E':True}
print(in_stock_status['F-150'])
in_stock_only = [{x:y} for x,y in in_stock_status.items() if y == True]
print(in_stock_only)
in_stock_dict = {x:y for x,y in in_stock_status.items() if y == True}
print(in_stock_dict)
mustang_stock = in_stock_status['Mustang']
print(mustang_stock)
in_stock_status['Explorer'] = False
print(in_stock_status)

# Input output
my_file = open('test.txt')
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
file_content = my_file.readlines()
for i in file_content:
    if 'Hazel' in i:
        print(i)
my_file.close()
with open('test.txt') as my_file:
    content = my_file.readlines()
    for i in content:
        if 'Hudson' in i:
            print(i)
with open('test.txt', mode='w') as my_file:
    my_file.write('Ollie,Newcomb,7')
with open('test.txt') as my_file:
    print(my_file.read())
# mode='r' or 'w', 'a', 'r+', 'w+'

