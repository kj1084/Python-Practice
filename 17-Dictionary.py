marks={"Math":90,"Science":85,"English":88}
print(marks)
print("Marks in Math:", marks["Math"])
marks["Hindi"]=96
print(marks)
len(marks)
print("Total number of subjects is :",len(marks))
for subject, score in marks.items():
    print(subject, ":", score)
highest=0
if score>highest:
    highest=score
print("Top Subject:", subject)
print("Top Score:", highest)