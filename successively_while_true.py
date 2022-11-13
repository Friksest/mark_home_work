"""
n = 1
while n <= 10:
    print(n)
    n +=1
"""

start_n = int(input('Enter first numerik: '))
end_n   = int(input('Enter last numerik: '))

if start_n < end_n:
    n = start_n
    while n <= end_n:
        print(n)
        n += 1
else:
     n = start_n
     while n >= end_n:
        print(n)
        n -= 1