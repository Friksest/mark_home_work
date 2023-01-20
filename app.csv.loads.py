import csv

def loadStats():
    file_name = "pop070100_20230120-041050.csv"
    file = open(file_name, "r")

    file_reader = csv.reader(file, delimiter = ",")

    rows = []
    for row in file_reader:
        rows.append(row)  # bidimentional list/array
        
    return rows
###################
data = loadStats()
# for row in data[4:12]:
#     if len(row) >=1:
#         print(f"{row[0]:>20s}", end="|")   # s - string
#         for cell in row[1:8]:
#             print(f"{cell:>3}", end="|")
#         
#     print("\n", "-" * 55)


# HW1 - REFACTOR CODE:
#       print total for 7 cells

def printByCountry(country_name, year = 2014):
    start_year = 2014
    period = year - start_year
    total_p = 0
    for row in data[4:]:
        if len(row) >=1:
            if row[0] == country_name:
                print(f"{row[0]:>20s}", end="|")   # s - string
                for cell in row[1 + period * 7:8 + period * 7]:              
                    print(f"{cell:>3}", end="|")
                    if cell == "-":
                        cell = 0
                    else:
                        a = int(cell)
                        total_p += a  
                print(f"{total_p:>3}|","\n")

############################################                
printByCountry("Brazilia", 2017)
