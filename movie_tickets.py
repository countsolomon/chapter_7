# < 3 tickets are free
# 3 < x < 12 tickets $10
# 12 < x tickets are 15

prompt = "\nWhat is your age? "
prompt += "\nEnter. 'quit' when you are finished entering your age. "

while True: 
    age = input(prompt)
    if age == 'quit':
        break
    elif age <= 3:
        print(f"your ticket price is free!")
    elif age >= 3 and <= 12:
        print(f"your tickets are 10 dollars")
    else:
        print(f"considering you are {age}. you will recieve the price of regular admission.\nyour admission price is 15 dollars.")
