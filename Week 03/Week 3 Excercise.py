#quiz game, where program will ask some questions to user and will took user answers as input, 
# if answer right it will print "correct answer", otherwise icorrect, and after ending the questions 
# program will show score to user.

ready = input("Are you ready? ").lower()
if ready != "yes":
    print("Ok, comeback when you are ready :)")
    quit()

print("Welcome to the quiz game!")

score = 0

question = input("How many built in data types in python? ").lower()
if question == "14":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

question = input("Which brackets used for tuple? [], {}, ()").lower()
if question == "()":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

question = input("What will be the sytax to check the lenght of list? ").lower()
if question == "len()":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

question = input("Does list allows duplication of items? ").lower()
if question == "yes":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

question = input("Which function used to add a item at the end of list? ").lower()
if question == "append function":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("Quiz Completed!")
print("You got " + str(score) + " correct answers")
print("You got " + str(score/5*100) + "%")