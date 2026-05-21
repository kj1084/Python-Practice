score=0
print("Q1. Capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Chennai")
attempts=0
while attempts<2:
    answer=input("Enter your answer: ")
    if answer=='b':
        score+=1
        print("Correct Answer!😎")
        break
    attempts+=1
    if attempts==2:
        print("Wrong Answer!😔 Try Next Question!")
print("Q2. Capital of Madhya Pradesh?")
print("a) Bhopal")
print("b) Indore")
print("c) Gwalior")
attempts=0
while attempts<2:
    answer=input("Enter your answer: ")
    if answer=='a':
        score+=1
        print("Correct Answer!😎")
        break
    attempts+=1    
    if attempts==2:
        print("Wrong Answer!😔 Try Next Question!")
print("Q3. Capital of Maharashtra?")
print("a) Mumbai")
print("b) Pune")
print("c) Nagpur")
attempts=0
while attempts<2:
    answer=input("Enter your answer: ")
    if answer=='a':
        score+=1
        print("Correct Answer!😎")
        break
    attempts+=1
    if attempts==2:
        print("Wrong Answer!😔 Quiz Over!")
print(f"Your final score is: {score}")
if score==3:
    print("Excellent!🏆")
elif score==2:
    print("Good job!👍")
elif score==1:
    print("Not Bad!🙂")
else:
    print("Better luck next time! Keep learning!📚")