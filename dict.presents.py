# multy level dict



# HW1: given that a user inputs group name and student name from KB
#       set presence of the given student as True

# HW2: given that a user inputs group name and student name from KB
#       print "{student name} is present!" or "{student name} is absent!"


# university["py bigginers"]["Jane"] = True
# print(university["py bigginers"]["Jane"])

# print("Mark" in university["py advanced"])

# print(university.keys())
# print(university["py bigginers"].values())

# university["py bigginers"]["Alex"] = True
# print(university)

from os import system

university = {
    "py bigginers":{
        "Jake": True,
        "Jane": False
    },
    "py advanced": {
        "Mark":True,
        "Pete":True,
        "Marry":False
    }
}
system("clear")
group_name = input("Input group (py bigginers/py advanced) > ")
st_name = input("Student name > ")
if st_name in university[group_name]:
    university[group_name][st_name] = True
else:
    university[group_name][st_name] = True
print(university[group_name])


check_group = input("Input student's group to check: >")
check_name  = input("Input student name to check: >")
if university[check_group][check_name] == True:
    print(f"Student {check_name} is present!")
else:
    print(f"Student {check_name} is empty!")























