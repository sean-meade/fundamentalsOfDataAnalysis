# Collatz operation is done on positive integers.
# 1. If the number is even, divide it by two.
# 2. If the number is odd, triple it and add one.

# starting integer
n = int(input("Please enter a positive integer:"))

# while number is not 1
while n != 1:
    # print current number
    print(int(n))
    # if number is even
    if n % 2 == 0:
        # divide number by 2
        n = n // 2
    # Otherwise (so the number is odd)
    else:
        # multiply by 3 and add 1
        n = (n * 3) + 1
# print final number (should be 1)
print(int(n))