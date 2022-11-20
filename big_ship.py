# small_ship = int(input("Sign small ship position: "))
big_ship   = int(input("Sign big ship position: "))
print()
for x in range(1,11):
    if x == big_ship:
        print( "wWw", end="" )
    else:
        print( "~", end="" )

print("\n")