
                                    #conditional statements

# Conditional statements are used to perform different actions based on different conditions.
# In Python, we have the following conditional statements:
# 1. if statement
# 2. if else statement
# 3. else if statement
# 4. Nested if statement

                                    # 1. if statement
# if condition:
#     statement

age=20
if age >= 18:
    print("Your Elgible for Voting ")

                                    #if else statement
# if condition:
#     statement
# else:
#     statement

age=18
if age < 20:
    print("Your elgible for Driving ")
else:
    print("your not elgible for driving")

                                     #else if statement

# if condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

Marks = int(input("Enter your Marks : "))
if Marks > 90:
    print("Your Grade is A")
elif Marks > 80:
    print("Your grade is B")
else:
    print("Your grade is c")
    

                                  # Nested if statement
# if condition:
#     if condition:
#         statement
#     else:
#         statement
# else:

age = 18
    
grade = "B"

if age >= 18:

            if grade == "A":
                    print("You are an adult with an A grade.")

            else:
                    print("You are an adult with a grade other than A.")

else:
            print("You are a minor.")