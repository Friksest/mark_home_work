

def inputInt( message ):
    value = int(input("Enter some value: "))
    return value
def inputFloat( message ):
    value = float(input("Enter some value: "))
    return value
def inputBoolean( message ):
    value = bool(input("Enter some value: "))
    return value


n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")

print( n + m )