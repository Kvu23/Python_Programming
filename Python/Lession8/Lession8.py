# conditionals statements if else 

age = 18

if (age >= 18):
    print("can apply for vote and licence")
else:
    print("Can't apply for vote and licences")


#Example of light

light = "green"

if(light == "red"):
    print("stop!")
elif(light == "green"):
    print("Go!")
elif(light == "yellow"):
    print("Wait!")
else:
    print("not sure what to do")
    
    
#Example of Marks via conditional statements

marks = int(input("enter marks: "))

if(marks >= 90):
    print("Grade A")
elif((marks >= 80) and (marks < 90)):
    print("Grade B")
elif((marks >= 70) and (marks < 80)):
    print("Grade C")
else:
    print("Grade D")

print("end of code\n\n")


#example of nesting If

age = int(input("enter age"))

if(age >= 18):
    if (age > 80):
        print("can not drive")
    else:    
        print("Can drive")
else:
    print("Can not drive")
    

    


    

