score=0
print("Q1. Capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Chennai")
while True:
    answer=input("Enter your answer: ")
    if answer=='b':
        score+=1
        print("Correct Answer!😎")
        break
    else:
        print("Wrong Answer!😔 Try Again!")
