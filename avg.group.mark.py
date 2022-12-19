from os import system

group_marks = {
     "John":   9.5,
     "Marry": 10.0,
     "Jane":   8.0
  }
system("clear")

x = 0
for values in group_marks:
    group_marks[values]
    x += group_marks[values]
a = x / len(group_marks)
group_marks["average"] = round(a,2)

for name in group_marks:
    print(name, group_marks[name])

# len(group_marks)     - определяет колличесвто объектов в dict

# print(type(group_marks["John"])) - опеределяет тип значения в discription