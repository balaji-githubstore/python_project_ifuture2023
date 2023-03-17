# tuple is mutable
colors = ["red", "green", "yellow", "blue", "green"]

print(colors[3])
print(type(colors))

print(colors)

colors.append("pink")

print(colors)

# insert black at index 1

colors.insert(1, "black")

print(colors)
# remove green from colors
# colors.remove("green")
count = colors.count("green")
print(count)

# colors.remove("green")
# colors.remove("green")
print(colors[0])
colors.remove(colors[0])
print(colors)

print(len(colors))

print(colors)
removed_item = colors.pop()
print(colors)

print(removed_item)

numbers = [98.2, 88, 78.1, 98]

print(type(numbers))

print(type(numbers[0]))
print(type(numbers[1]))

# tuple is immutable
signal = ("red", "yellow", "green", "red")

print(signal[1], signal[2])
# print(signal[1:])

desired_cap = {
    "platformName": "android",
    "deviceName": "oneplus",
    "platformVersion": 8
}

print(desired_cap)
print(type(desired_cap))
print(desired_cap["deviceName"])

student_record = {
    "name": "john",
    "mail_id": "john@gmail.com",
    "marks": [98, 45, 78, 65, 55],
    "sports": {
        "indoor": "chess",
        "outdoor": "hockey"
    }
}
print(student_record["marks"])
print(type(student_record["marks"]))
print(student_record["marks"][0])
all_marks = student_record["marks"]
print(all_marks[0])

print(student_record["sports"]["outdoor"])

check=True
print(check)
print(type(check))

print('chess' in student_record)

a = ['foo', 'bar2', 'baz', 'qux', 'corge']

while a:
    if len(a) < 3:
        break
    print(a.pop())
print('Done.')


# b=['a']
#
# b[1]='j'
# print(b)

d = {'a': 0, 'b': 1, 'c': 0}

if d['a'] > 0:
   print('yeah!')
elif d['b'] > 0:
   print('yeah!')
elif d['c'] > 0:
   print('ok')
elif d['d'] > 0:
   print('ok')
else:
   print('not ok')