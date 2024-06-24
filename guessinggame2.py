import time
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
#Welcome the user
print("       Welcome to the HOME SWEET HOME Game!")
time.sleep(1)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")

#Chances
chances=1
print("You have to pick", chances,"correct answer.\nYou will get 1 score if you pick a correct answer.\n")
time.sleep(2)

#score
score=0

#question 1
print("==================================================")
question_1=print("1) I AM USUALLY USED IN THE MORNING AT THE KITCHEN. WHO AM I?\n(A) SHAVER\n(B) TOASTER\n(C) VACUUM\n(D) HAIR DRYER\n\n")
answer_1= "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("OPPSS...INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_1, "\n\n")

time.sleep(2)

#question 2
print("==================================================")
question_2 = print("2)I HAVE A PILLOW AND SHEETS?\n(A) BED\n(B) TABLE LAMP\n(C) FAN\n(D) TELEVISION\n\n")  
answer_2 = "a"

for i in range(chances):
    answer = input("answer: ")
    if (answer.lower() == answer_2):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("OPPSS...INCORRECT!\n ")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_2, "\n\n")

time.sleep(2)

#question 3
print("==================================================")
question_3 =print("3)  I HAVE ARMS AND COZY. I AM.....?\n(A) RICE COOKER\n(B) CLOCK\n(C) SOFA\n(D) DINING TABLE\n\n")
answer_3= "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("OPPSS...INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_3, "\n\n")

time.sleep(2)

#question 4
print("==================================================")
question_4 =print("4)  I CLEAN THE CARPET. WHO AM I?\n(A) VACUUM\n(B) DESK\n(C) TOASTER\n(D) AIR FRYER\n\n")
answer_4= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("OPPSS...INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS",answer_4, "\n\n")

time.sleep(2)

#question 5
print("==================================================")
question_5 =print("5)  I SIT ON THE TABLE. EVERY MORNING I'LL SING A SONG?\n(A) KETTLE\n(B) TABLE LAMP\n(C) FRAME\n(D) ALARM CLOCK\n\n")
answer_5= "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("OPPSS...INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_5, "\n\n")

time.sleep(2)

#print the score
print("==================================================")
while score >=2:
    print("         Well done! Your Score was", score)
    break

while score <2:
    print("    Better luck next time! Your score was",score)
    break

#Goobye message
print("  Thank you for playing the HOME SWEET HOME Game!")
print("                See you again!")
print("==================================================")