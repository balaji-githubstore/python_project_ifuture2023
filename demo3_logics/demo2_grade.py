mark = 195

if mark>100 or mark<0:
    print("Invalid input")
elif mark >= 90:
    print("Grade A")
elif mark >= 80 and mark <= 89:
    print("Grade B")
elif mark >= 60 and mark <= 79:
    print("Grade C")
else:
    print("Failed, Please re-attempt")
