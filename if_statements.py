# if = do same code if some condition is true 
        # Else do something else

age = int(input("enter your age: "))

if age >= 100:
    print("you are too old to sign up")
elif age>= 18:
    print("you are too now sign up!")
elif age < 0:
    print("you haven't been born yet!")

else:
    print("you must be 18+ to sign up")