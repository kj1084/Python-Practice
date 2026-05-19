file=open("Radha.txt","w")
file.write("Aru is a Good player!")
file.close()

file=open("Radha.txt","r")
print(file.read())
file.close()

file=open("Radha.txt","a")
file.write("\nRenuka is a Good Bowler!")
file.close()

file=open("Radha.txt","r")
file.readline() #used to print 2nd line of the file data 
print(file.readline())
file.close()

file=open("Radha.txt","a")
file.write("\nShefali is a Good Batter!")
file.close()

file=open("Radha.txt","r")
file.readline() #used to print 2nd line of the file data
file.readline() #used to print 3rd line of the file data  
print(file.readline())
file.close()

file=open("Radha.txt","r")
lines=file.readlines()
print("Number of lines in the file:", len(lines))
file.close()

file=open("Radha.txt","r")
text=file.read()
words=text.split()
print(words)
print("Number of words in the file:", len(words))
file.close()

file=open("Radha.txt","a")
file.write("\nSneh is a Good Finisher!")
file.close()

file=open("Radha.txt","r")
text=file.read()
if "Sneh" in text:
    print("The name 'Sneh' is present in the file.")
else:
    print("The name 'Sneh' is not present in the file.")
file.close()    