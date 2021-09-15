#make the following quiz
#asks 10 multiple choice questions
#randomizes potential answers
#records end result
#gives the user a grade after the quiz is over
from is_num import is_num
from random import shuffle

score = 0
grade = ""

response0 = ""
response1 = ""
response2 = ""
response3 = ""
response4 = ""
response5 = ""
response6 = ""
response7 = ""
response8 = ""
response9 = ""

choices0 = ["50", "15", "55", "105"]
choices1 = ["20", "25", "7", "19"]
choices2 = ["42", "-42", "56", "-56"]
choices3 = ["51", "42", "54", "49"]
choices4 = ["133", "123", "140", "99"]
choices5 = ["83", "78", "80", "81"]
choices6 = ["120", "105", "128", "144"]
choices7 = ["5", "4", "7", "3"]
choices8 = ["382", "378", "374", "388"]
choices9 = ["21", "19", "24", "20"]

shuffle(choices0)
shuffle(choices1)
shuffle(choices2)
shuffle(choices3)
shuffle(choices4)
shuffle(choices5)
shuffle(choices6)
shuffle(choices7)
shuffle(choices8)
shuffle(choices9)

print("For this quiz, please use exact numerical responses.")
print("This is a multiple choice quiz.")
print("The answers to the question will print on the line above the question.")

print(choices0)
response0 = is_num(f"What is 5 * 10?\n")
print(choices1)
response1 = is_num(f"What is 100 / 5?\n")
print(choices2)
response2 = is_num(f"What is -6 * -7?\n")
print(choices3)
response3 = is_num(f"What is 17 * 3?\n")
print(choices4)
response4 = is_num(f"What is 110 + 23?\n")
print(choices5)
response5 = is_num(f"What is 90 - 7?\n")
print(choices6)
response6 = is_num(f"What is 8 * 15?\n")
print(choices7)
response7 = is_num(f"What is 170 / 34?\n")
print(choices8)
response8 = is_num(f"What is 240 + 142?\n")
print(choices9)
response9 = is_num(f"What is 9 + 10?\n")

if response0 == "50":
    score+=1
if response1 == "20":
    score+=1
if response2 == "42":
    score+=1
if response3 == "51":
    score+=1
if response4 == "133":
    score+=1
if response5 == "83":
    score+=1
if response6 == "120":
    score+=1
if response7 == "5":
    score+=1
if response8 == "382":
    score+=1
if response9 == "21":
    score+=1

if score == 9 or score == 10:
    grade = "A"
elif score == 8:
    grade = "B"
elif score == 7:
    grade = "C"
elif score == 6:
    grade = "D"
else:
    grade = "F"

print("Your score was " + str(score))
print("Your grade is " + str(grade)+ ".")


