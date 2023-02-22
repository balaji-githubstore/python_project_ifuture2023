num = 10

if num < 0:
    print("The number is negative ", num)
elif num == 0:
    print("It's zero!!")
else:
    print("The number is positive ", num)

page_number = 250

# check between 100 and 200
if page_number >= 100:
    if page_number <= 200:
        print("Yes! between 100 and 200")

if page_number >= 100 and page_number <= 200:
    print("Yes! between 100 and 200")

if 100 <= page_number <= 200:
    print("Yes! between 100 and 200")

mark = 60
if (mark >= 90):
    print("Grade is A")
elif (mark > 80 and mark < 89):
    print("Grade is B")
elif (mark > 60 and mark < 79):
    print("Grade is C")
elif (mark == 0 and mark <= 60):
    print("Grade is D")
else:
    (print("Invalid number"))
