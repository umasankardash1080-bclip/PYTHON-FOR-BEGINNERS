mark = int(input("enter your mark :\n"))
if(mark>=90):
    greade = "A"
elif(mark<90 and mark>=80):
    grade = "B"
elif(mark<80 and mark >=60):
    grade = "C"
elif(mark<60 and mark>=30):
    grade = "D"
else:
    print("your are failed try again best of luck")
print(grade)