'''
Write a function called name_printer that takes in two string parameters first_name and last_name and prints a greeting.
Here are some sample function calls - notice the default parameters

name_printer("Norman","Roberts")
name_printer("Bob")
name_printer()

Hello, Norman Roberts!
Hello, Bob Doe!
Hello, John Doe!
'''

def name_printer(first_name="Starla",last_name="Doe"):
    print(f"Hello, {first_name} {last_name}!")

'''
Write a function that takes in two parameters, a person's name
and their favorite color. Print out their name in the form
"<name> the fierce, <color> eyed warrior"

If they choose not to enter a favorite color, make the default color
yellow

'''

def warrior(name,color="yellow"):
    print(f"{name} the fierce, {color} eyed warrior")

def main():
    warrior("Jonathan","blue")
    warrior("John")
    blackjack(1,5,8)
    blackjack(0,22,8)
    blackjack(10,11,1)
    blackjack(4,8,12)



'''
Write a function called blackjack that takes in three integer parameters. The numbers
should be between 1 and 11. If their sum is less than or equal to 21, print the sum. If
the sum exceeds 21 and there is an 11, print the sum reduced by 10. If the sum exceeds 21,
print BUST. If an integer outside of 1-11 is entered, print ERROR.
'''

def blackjack(hit_1,hit_2,hit_3):
    sum = hit_1 + hit_2 + hit_3
    if 1< sum <= 21:
        print(sum)
    if 21<sum<1:
        print(sum)
    if sum<21 and hit_1==11 or hit_2==11 or hit_3==11:
        print(sum-10)
    elif hit_1<1 or hit_1>11 or hit_2<1 or hit_2>11 or hit_3<1 or hit_3>11:
        print("ERROR")



#def main():
    #name_printer("Norman","Brewer")
    #name_printer("Wilson")



if __name__ == '__main__':
    main()