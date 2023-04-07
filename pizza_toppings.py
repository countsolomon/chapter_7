#while loop going through toppings. 
#print message once the topping has been entered by the user. 

prompt = "\n welcome to pizza planet. what can i put on your pizza? "
prompt += "\nEnter 'quit' when you are finished. \n"

#while true loops will look for a break within the loop to tell the loop to stop rolling. 

while True:
    topping = input(prompt)
    
    if topping =='quit':
        break
    else: 
        print(f"I am going to go  ahead and add {topping} to your pizza. \nfeel free to add another topping. \nthank you. ")


