# 7-10 exercise. dream vacation.
#a program that polls the user about their dream vacation. 

dream_spot = {}
polling_active = True

prompt = '\nWhat is your dream vacation? '
prompt_2 = '\nWould you like to let another person respond? (yes/no) '

while polling_active:
    #ask the user for their name. 
    name = input('\nWhat is your name? ')
    vacation_spot = input(prompt)
    
    #t store inside the dictionary. 
    dream_spot[name] = vacation_spot
    
    #is the poll still active?
    keep_going = input(prompt_2)
    
    if keep_going == 'yes':
        continue
    elif keep_going == 'no':
        polling_active = False

#polling results
print(f"\n---Polling Results---")
for name, vacation_spot in dream_spot.items():
    print(f'{name.title()} would like to go to {vacation_spot}')

    