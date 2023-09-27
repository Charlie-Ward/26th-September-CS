count = 0
first = int(input("Enter lower bound: "))
last = int(input("Enter upper bound: "))
n = first
while n <= last:
    if n != 0:
        if n % 5 == 0:
            count += 1
        elif n % 3 == 0:
            count += 1
    n += 1
print('Values divisible by 3 or 5:', count)