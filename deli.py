#a simple deli program
#exercise 7-8
#exercise 7-9 removing all instances of pastrami. 
#the deli has run out of pastrami

sandwich_orders = ['chicken salad', 'pastrami', 'ham', 'pastrami', 'roast beef', 'chicken, bacon, ranch', 'pastrami']
finished_sandwiches = []

#7-9 while loops that removes all pastrami. 
print('\n Notice: unfortunately we are out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders:
    current_sand = sandwich_orders.pop()
    print(f"\nMaking sandwich {current_sand.title()}")
    #append the created sandwich to the new list. 
    finished_sandwiches.append(current_sand)
print(f'\n')
#print the sandwhiches that have been completed. 
for sand in finished_sandwiches:
    print(f'{sand.title()} sandwich is finished.')
