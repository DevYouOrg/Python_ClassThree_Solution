# Exercise One

my_number = 5
user_guess = int(input("Guess a number (1-10): "))

if user_guess == my_number:
    print("You are correct")
    
# Exercise Two

income = int(input("Enter income amount: "))
credit_score = int(input("Enter credit score: "))

if income > 50000 and credit_score > 650:
    print("You are approved!")

# Exercise Three

secret_word = "password"
user_guess = input("Guess secret word: ")

if secret_word == user_guess:
    print("You guessed correctly")
else:
    print("You guessed incorrectly")

# Exercise Four

first_num = int(input("Enter a number: "))
second_num = int(input("Enter a number: "))

menu_choice = input("Would you like to [1]Add [2]Subtract [3]Multiply [4]Divide?: ")

if menu_choice == "1":
    print(f"{first_num} + {second_num} = {first_num+second_num}")
elif menu_choice == "2":
    print(f"{first_num} - {second_num} = {first_num-second_num}")
elif menu_choice == "3":
    print(f"{first_num} * {second_num} = {first_num*second_num}")
elif menu_choice == "4":
    print(f"{first_num} / {second_num} = {first_num/second_num}")
else:
    print("Please enter a valid choice.")
