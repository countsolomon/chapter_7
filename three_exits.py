#exercise 7-6 in crash course book. 
#movie_tickets.py - exerciese needs the following comments outlined. 
#use a conditional test within the 'while statement' to quit the loop
#'active' variable 
#use a 'break' statement when the user enters quit

prompt = "\nEnter pizza toppings that you would like to have on your pizza."
prompt += "\nEnter 'quit' to end the program, type 'quit'. "

active = True
while active:
    topping = input(prompt)
    
    if topping == 'quit':
        active = False
    else: 
        print(f"\nI am going to go  ahead and add {topping.title()} to your pizza. \nFeel free to add another topping!\nThank you!")

